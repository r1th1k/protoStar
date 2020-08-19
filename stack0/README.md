# STACK0
 
in this challenge on viewing the source code from []() i understand that the program 

have two variables called modified and buffer where the buffer variable can hold upto a 64 characters

and  the interesting part is it uses *gets* for getting the input on viewiing the man page it is clear that 

gets will get anything we enter without filtering or checking the number of characters we enter

so we can use this to exploit a simple buffer overflow all you need to do is enter a string that is more than

64 characters and you will get the success output in other words you had changed the modified variable

But if you need to know what happens, follow along......

use gdb to examine the binary `gdb ./stack0`

set the disassemble flavor to intel as it is easy to understand just by looking`set disassembly-flavor intel`

now view the main function part `disassemble main`

you will get the following output:

```
0x080483f4 <main+0>:	push   ebp                        #base pointer
0x080483f5 <main+1>:	mov    ebp,esp					  #assign the value of stack pointer to base pointer
0x080483f7 <main+3>:	and    esp,0xfffffff0			  
0x080483fa <main+6>:	sub    esp,0x60					  #sub 0x60 from esp
0x080483fd <main+9>:	mov    DWORD PTR [esp+0x5c],0x0   #modified variable set to 0
0x08048405 <main+17>:	lea    eax,[esp+0x1c]
0x08048409 <main+21>:	mov    DWORD PTR [esp],eax
0x0804840c <main+24>:	call   0x804830c <gets@plt>
0x08048411 <main+29>:	mov    eax,DWORD PTR [esp+0x5c]
0x08048415 <main+33>:	test   eax,eax                    #check wheter the modified variable is still zero
0x08048417 <main+35>:	je     0x8048427 <main+51>        #if true then jump to 0x8048427
0x08048419 <main+37>:	mov    DWORD PTR [esp],0x8048500  
0x08048420 <main+44>:	call   0x804832c <puts@plt>       #print "you have changed the 'modified' variable\n"
0x08048425 <main+49>:	jmp    0x8048433 <main+63>
0x08048427 <main+51>:	mov    DWORD PTR [esp],0x8048529
0x0804842e <main+58>:	call   0x804832c <puts@plt>		  #print "Try again?\n"
0x08048433 <main+63>:	leave  
0x08048434 <main+64>:	ret    

```

read the above comments to understand the working of the program