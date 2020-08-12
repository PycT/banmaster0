from clueminer import secureClueMiner;

test_message = "Aug  9 06:24:53 domain8 sshd[98086]: User root from 111.90.141.98 not allowed because not listed in AllowUsers";
test_message1 = "Aug  9 06:24:53 domain8 sshd[98086]: User root from - not allowed because not listed in AllowUsers";

miner1 = secureClueMiner();

print(miner1.get_time_stamp(test_message));
print(miner1.get_ip_address(test_message));

print(miner1.score_message(test_message));