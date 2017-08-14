#!/usr/bin/perl

use warnings;
use strict;

use FindBin qw($Bin);
use lib "$Bin/ZabbixAPI";

use Data::Dumper;
use ZabbixAPI;
use Getopt::Long;
my $username = 'Admin';
my $password = 'zabbix';
my $api_url = 'http://localhost/zabbix/api_jsonrpc.php';

my $zbx;
my $params;
my $json;
my $result;
my $lang = "EN";

GetOptions(
    "api_url=s" =>  \$api_url,
    "password|p=s"       => \$password,
    "username|u=s"      =>   \$username,
    "lang=s"      =>   \$lang,
#    "file=s"             =>    \@files
   
) or die("Error in command line arguments\n");



$zbx = ZabbixAPI->new( { api_url=>$api_url, username => $username, password => $password } );

$zbx->login();


my $temp_dir = $ARGV[0] or die "Please provide directory with templates as first ARG\n";

    opendir my $dir, $temp_dir  or die "Cannot open directory: $temp_dir\n";
    my @dir_files;
    if ($lang eq 'ALL') {
       @dir_files = grep { /\.xml$/ && -f "$temp_dir/$_" } readdir($dir);
    }
    else {
       @dir_files = grep { /_$lang\.xml$/ && -f "$temp_dir/$_" } readdir($dir);
    }
    
    closedir $dir;

    foreach my $file (@dir_files) {
            print $file."\n";
            $zbx->import_configuration_from_file("$temp_dir/$file");
    }


$zbx->logout();