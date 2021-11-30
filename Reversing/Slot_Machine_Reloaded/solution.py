import requests
import json
from randcrack import RandCrack
import math

PRINTABLE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+-/:.;<=>?@[]^_`{}"

def flag_list():
    flag = []
    for i in range(32):
        flag.append([])
    return flag

def setup_remote():
    s = requests.session()
    s.get("http://slot-machine-reloaded.csa-challenge.com")
    return s

def remote_spin(s):
    r = s.get("http://slot-machine-reloaded.csa-challenge.com/spin/?coins={}".format(0))
    j = json.loads(r.text)
    print(j['result'])
    return j['result']

def make_printable_list(printable):
    printable_list=[]
    printable_list[:0]=PRINTABLE
    return printable_list

def find_rand_num(result):
    printable_list = make_printable_list(PRINTABLE)
    rand_num = ''
    for letter in result:
        rand_num += format(printable_list.index(letter),'06b')
    return rand_num

def get_all_bins(s):
    nums = []
    for i in range(200):
        result = remote_spin(s)
        nums.append(find_rand_num(result))
    return nums

def split_bins(result_list):
    nums_int_list = []
    for i in result_list:
        for j in reversed(range(0,192,32)):
            nums_int_list.append(i[j:j+32])
    return nums_int_list

def split_bins_to_int(spl_bin_list):
    split_bin_int_list = []
    for i in spl_bin_list:
        split_bin_int_list.append(int(i,2))
    return split_bin_int_list

check_flag = False
flag_chr_list = flag_list()
while check_flag == False:

    rc = RandCrack()
    sess = setup_remote()
    # Translate result of spins to indexes of all chars and then convert the index number to binary
    nums_list = get_all_bins(sess)
    # The cracker fed with 32 bit at a time and from right to left, so every 192 bits we count 32 from right to left
    split_bin_list = split_bins(nums_list)
    # Make all 32 bits to integer for the cracker
    split_int_list = split_bins_to_int(split_bin_list)

    # Feeding the cracker
    for i in range(576,1200):
        rc.submit(split_int_list[i])


    for i in range(100):

        result = remote_spin(sess)
        rand_num = format(rc.predict_randbelow((1 << (32*len(f'{len(PRINTABLE) - 1:b}'))) - 1),
                    '#0%db' % (32*int(math.log(len(PRINTABLE), 2)) + 2))[2:]
        counter = 0
        for j in range(0, 192 ,6):
            ind = int(rand_num[j:j+6],2)
            if ind == 0:
                flag_chr_list[counter] = result[counter]
            counter += 1

        #check flag
        if [] not in flag_chr_list:
            check_flag = True

print("".join(flag_chr_list))
