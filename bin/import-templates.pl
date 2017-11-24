#!/usr/bin/perl

use warnings;
use strict;

binmode(STDOUT,':utf8');
binmode(STDERR,':utf8');
use FindBin qw($Bin);
use lib "$Bin/ZabbixAPI";

use Data::Dumper;
use ZabbixAPI;
use Getopt::Long;
my $username = 'Admin';
my $password = 'zabbix';
my $api_url = 'http://localhost/zabbix/api_jsonrpc.php';
my $filter = ''; #use this filter to import only files that contain this sequence. XML is hardcoded.

GetOptions(
    "api_url|url=s" =>  \$api_url,
    "password|p=s"       => \$password,
    "username|u=s"      =>   \$username,
    "filter|lang=s"      =>   \$filter,
   
) or die("Error in command line arguments\n");

my $zbx = ZabbixAPI->new( { api_url=>$api_url, username => $username, password => $password } );

my $temp = $ARGV[0] or die "Please provide directory with templates as first ARG or the XML file with template\n";
if (-d $temp) {

    opendir my $dir, $temp or die "Cannot open directory: $temp\n";
    
    my @templates = grep { /${filter}.*\.xml$/ && -f "$temp/$_" } readdir($dir);

    closedir $dir;
	die "No templates found in directory $temp!\n" if @templates == 0;

    $zbx->login();
    foreach my $file (sort { $a cmp $b } (@templates)) {
        print "$temp/$file\n";
        $zbx->import_configuration_from_file("$temp/$file");
    }
    $zbx->logout();

}
elsif (-f $temp) {
    $zbx->login();	
    print $temp."\n";
    $zbx->import_configuration_from_file($temp);
    $zbx->logout();
}