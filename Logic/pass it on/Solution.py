from subprocess import Popen, PIPE
import time

possible =  '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_}{!#$%&@'
p = Popen(['Pass_it_on.exe'], stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True)

flag = ''
counter = 26
searching = True
while searching:
    time_arr = []
    for i in possible:
        please_enter = p.stdout.readline()
        if 'Please enter your password to log in' not in please_enter:
            print(please_enter)
            done = True
            break
        start = time.time()
        p.stdin.write(flag + i + "-" * counter)
        p.stdin.write("\n")
        line = p.stdout.readline()
        end = time.time()
        print line.rstrip()
        time_arr.append(end-start)
    counter -= 1
    flag += possible[time_arr.index(max(time_arr))]
    print flag
