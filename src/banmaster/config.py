secure_log_path = "/var/log/secure";

secure_log_score_tokens = \
{
    "Invalid user": 3,
    "User root": 5,
    "Failed password": 2
};

secure_log_score_limit = 10;

#firewall-cmd --permanent --ipset=some_set --add-entry=xxx.xxx.xxx.xxx

firewalld_ipset_name = "ips2drop";

#####################################################
#           technical section                                                                                           #
#####################################################

# time_stamp_pattern = "";
ip_address_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}";
abuse_report_mail_pattern = r"abuse@[a-zA-Z]+\.[a-zA-Z]+";

#####################################################