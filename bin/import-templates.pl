#!/usr/bin/perl

use warnings;
use strict;

binmode( STDOUT, ':utf8' );
binmode( STDERR, ':utf8' );
use FindBin qw($Bin);
use lib "$Bin/ZabbixAPI";

use Data::Dumper;
use ZabbixAPI;
use Getopt::Long;
my $username = 'Admin';
my $password = 'zabbix';
my $api_url  = 'http://localhost/zabbix/api_jsonrpc.php';
my $filter   = ''; #use this filter to import only files that contain this sequence. XML is hardcoded.
my $opt_help =0 ;
my $help = <<'END_PARAMS';

To import a single template:
    import-templates.pl [options] template.xml

     Options:
       --api_url,--url     Zabbix API URL, default is http://localhost/zabbix/api_jsonrpc.php
       --username,-u       Zabbix API user, default is 'Admin'
       --password,-p       Zabbix API user's password, default is 'zabbix'

To import all templates in the directory:
    import-templates.pl [options] dir_with_templates

     Options:
       --api_url,--url     Zabbix API URL, default is http://localhost/zabbix/api_jsonrpc.php
       --username,-u       Zabbix API user, default is 'Admin'
       --password,-p       Zabbix API user's password, default is 'zabbix'       
       --filter            Imports only files that contain filter specified in their filenames.
END_PARAMS
GetOptions(
    "api_url|url=s" => \$api_url,
    "password|p=s"  => \$password,
    "username|u=s"  => \$username,
    "filter|lang=s" => \$filter,
    "help|?"        => \$opt_help
) or die("$help\n");

if ($opt_help) {
    print "$help\n";
    exit 0;
}


my $zbx = ZabbixAPI->new( { api_url => $api_url, username => $username, password => $password } );

my $temp = $ARGV[0] or die "Please provide directory with templates as first ARG or the XML file with template.\n $help\n";
if ( -d $temp ) {

    opendir my $dir, $temp or die "Cannot open directory: $temp\n";

    my @templates = grep { /${filter}.*\.xml$/ && -f "$temp/$_" } readdir($dir);

    closedir $dir;
    die "No templates found in directory $temp!\n" if @templates == 0;

    $zbx->login();
    foreach my $file ( sort { $a cmp $b } (@templates) ) {
        print "$temp/$file\n";
        $zbx->import_configuration_from_file("$temp/$file");
    }
    $zbx->logout();

}
elsif ( -f $temp ) {
    $zbx->login();
    print $temp. "\n";
    $zbx->import_configuration_from_file($temp);
    $zbx->logout();
}
