from config import *;
import subprocess;
import sys;
import re;

termination_message = \
"""
\n*****\n
Usage:
    python whoismail.py xxx.xxx.xxx.xxx

    xxx.xxx.xxx.xxx - the ip address to mine an abuse report mail for
""";

def terminate():

    print(termination_message);
    exit();

def check_ip_validity(ip_address):
    
    return re.fullmatch(ip_address_pattern, ip_address);

def get_whois_output(ip_address):

    whois_result = subprocess.run(["whois", ip_address], capture_output = True);

    whois_lines = whois_result.stdout.decode().split("\n");

    return whois_lines;

def mine_abuse_report_mail(whois_lines):

    for the_line in whois_lines:

        if "abuse@" in the_line:
            mail_in_line = re.search(abuse_report_mail_pattern, the_line);
            if mail_in_line:
                return mail_in_line.group(0);

    return None;

def whoismail_pipeline(ip_address = None):

    if not ip_address:
        if len(sys.argv) < 2:
            terminate();

        ip_address = sys.argv[1];

    if not check_ip_validity(ip_address):
        terminate();

    whois_output_lines = get_whois_output(ip_address);
    the_email = mine_abuse_report_mail(whois_output_lines);

    return the_email;

def main():

    print("hi!");
    return 0;

if __name__ == "__main__":

    main();