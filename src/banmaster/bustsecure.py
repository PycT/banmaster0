import sys;
import os.path;
from config import *;
from clueminer import secureClueMiner;

termination_message = \
"""
\n*****\n
Usage:
    python bustesecure.py [path_to_log_file]

    default log to parse: /var/log/secure
""";

def terminate():

    print(termination_message);
    exit();

def main():

    if len(sys.argv) < 2:
        secure_log_file_path = secure_log_path; #secure_log_path is set in config.py
    else:
        secure_log_file_path = sys.argv[1];

    if not os.path.isfile(secure_log_file_path):
        print("\n*****\n{} is not a file.".format(secure_log_file_path))
        terminate();

    buster = secureClueMiner();

    busted_dictionary = {};

    messages_count = 0;

    with open(secure_log_file_path, "r") as log_file:

        for log_message in log_file:
            messages_count += 1;

            # print("{}. {}".format\
            #         (
            #             messages_count,
            #             log_message
            #         ));

            bust_score = buster.score_message(log_message);

            if bust_score > 0:

                busted_ip_address = buster.get_ip_address(log_message);

                if busted_ip_address in busted_dictionary:

                    busted_dictionary[busted_ip_address]["score"] += bust_score;
                    busted_dictionary[busted_ip_address]["messages"].append(log_message);

                else:

                    busted_dictionary[busted_ip_address] = {"score": bust_score, "messages":[]};
                    # busted_dictionary[busted_ip_address]["score"] = bust_score;
                    busted_dictionary[busted_ip_address]["messages"].append(log_message.rstrip());

                print("Busted! \n ip: {} \n score: {} \n {} \n***************".format\
                        (
                            busted_ip_address,
                            busted_dictionary[busted_ip_address]["score"],
                            log_message
                        ));

                log_message = log_file.readline();

    return busted_dictionary;

def print_ip_addresses(busted_dictionary):

    for ip_address in busted_dictionary:
        if busted_dictionary[ip_address]["score"] >= secure_log_score_limit: # secure_log_score_limit is defined in config.py
            print(ip_address);

    return 0;

def print_ip_addresses_and_score(busted_dictionary):

    for ip_address in busted_dictionary:
        if busted_dictionary[ip_address]["score"] >= secure_log_score_limit: # secure_log_score_limit is defined in config.py
            print("{} ({})".format(
                    ip_address,
                    busted_dictionary[ip_address]["score"]
                    ));

    return 0;

def print_ip_addresses_and_clues(busted_dictionary):

    for ip_address in busted_dictionary:
        if busted_dictionary[ip_address]["score"] >= secure_log_score_limit: # secure_log_score_limit is defined in config.py
            print("=======================================================");
            print("{} ({})".format(
                    ip_address,
                    busted_dictionary[ip_address]["score"]
                    ));
            for the_clue in busted_dictionary[ip_address]["messages"]:
                print(the_clue.rstrip());

    return 0;

if __name__ == '__main__':
    
    busted_dictionary = main();

    # print_ip_addresses(busted_dictionary);
    print_ip_addresses_and_score(busted_dictionary);
    # print_ip_addresses_and_clues(busted_dictionary);
