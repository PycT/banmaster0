from config import *;
import re;

class secureClueMiner:

    # time_stamp_pattern = "";
    ip_address_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}";

    score_tokens = secure_log_score_tokens; # secure_log_score_tokens are defined in config.py

    # secureCluesStructure = \
    # {
    #     "score":0,
    #     "messages": []
    # };

    def __init__(self):

        self.busted = {};

        return None;

    def get_time_stamp(self, message_string):
        return message_string[:15];

    def get_ip_address(self, message_string):
        the_ip_address = None;
        the_result = re.search(self.ip_address_pattern, message_string);
        if the_result:
            the_ip_address = the_result.group(0);
        return the_ip_address;

    def score_message(self, message_string):

        the_score = 0;
        for the_token in self.score_tokens:
            if the_token in message_string:
                the_score += self.score_tokens[the_token];

        return the_score;        