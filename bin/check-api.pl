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
my $api_url = 'http://localhost/api_jsonrpc.php';

my $zbx;
my $params;
my $json;
my $result;

GetOptions(
    "api_url=s" =>  \$api_url,
    "password|p=s"       => \$password,
    "username|u=s"      =>   \$username
) or die("Error in command line arguments\n");



$zbx = ZabbixAPI->new( { api_url=>$api_url, username => $username, password => $password } );
eval {
	$zbx->login();
};
if ($@) {
	die $@;
}
else {
	print "Zabbix API is ready\n";
	$zbx->logout();
}


