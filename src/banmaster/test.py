from clueminer import *;
from whoismail import *;
from bustsecure import *;

test_file_path = "../../temp/secure";

test_message = "Aug  9 06:24:53 domain8 sshd[98086]: User root from 111.90.141.98 not allowed because not listed in AllowUsers";
test_message1 = "Aug  9 06:24:53 domain8 sshd[98086]: User root from - not allowed because not listed in AllowUsers";
test_ip = "24.90.77.220";
test_invalid_ip = "24..77.220";


def clueminer_test():
    miner1 = secureClueMiner();
    print(miner1.get_time_stamp(test_message));
    print(miner1.get_ip_address(test_message));
    print(miner1.score_message(test_message));
    return 0;

def whoismail_test():

    assert check_ip_validity(test_ip);

    assert not check_ip_validity(test_invalid_ip);

    return 0;


print(whoismail_pipeline(test_ip));
