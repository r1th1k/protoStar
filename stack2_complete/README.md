# stack2

it is similiar to the second(stack1) challenge the only difference is instead of giving the value as an argument we set as environment variable

0x08048494 <main+0>:    push   ebp                          #push the base pointer to the stack                     
0x08048495 <main+1>:    mov    ebp,esp 
0x08048497 <main+3>:    and    esp,0xfffffff0 
0x0804849a <main+6>:    sub    esp,0x60                     #subtract 0x60 and form a stack frame
0x0804849d <main+9>:    mov    DWORD PTR [esp],0x80485e0 
0x080484a4 <main+16>:   call   0x804837c <getenv@plt>	    #call the getenv() function and get the value of greenie environment variable
0x080484a9 <main+21>:   mov    DWORD PTR [esp+0x5c],eax	    #mov eax(GREENIE env value) to this address [esp+0x5c]
0x080484ad <main+25>:   cmp    DWORD PTR [esp+0x5c],0x0	    #check if the environment variable is null or not
0x080484b2 <main+30>:   jne    0x80484c8 <main+52>	    #if it is not null jump to 0x80484c8
0x080484b4 <main+32>:   mov    DWORD PTR [esp+0x4],0x80485e8
0x080484bc <main+40>:   mov    DWORD PTR [esp],0x1
0x080484c3 <main+47>:   call   0x80483bc <errx@plt>	    #if environment variable is null show error
0x080484c8 <main+52>:   mov    DWORD PTR [esp+0x58],0x0
0x080484d0 <main+60>:   mov    eax,DWORD PTR [esp+0x5c]
0x080484d4 <main+64>:   mov    DWORD PTR [esp+0x4],eax
0x080484d8 <main+68>:   lea    eax,[esp+0x18]
0x080484dc <main+72>:   mov    DWORD PTR [esp],eax
0x080484df <main+75>:   call   0x804839c <strcpy@plt>	    #copy the environment variable to the buffer 
0x080484e4 <main+80>:   mov    eax,DWORD PTR [esp+0x58]
0x080484e8 <main+84>:   cmp    eax,0xd0a0d0a		    #check if the modified variable's value is 0x0d0a0d0a
0x080484ed <main+89>:   jne    0x80484fd <main+105>         #jump if not equal
0x080484ef <main+91>:   mov    DWORD PTR [esp],0x8048618
0x080484f6 <main+98>:   call   0x80483cc <puts@plt>	    #print the success message
0x080484fb <main+103>:  jmp    0x8048512 <main+126>	    #jump to the end of the program or leave the program
0x080484fd <main+105>:  mov    edx,DWORD PTR [esp+0x58]
0x08048501 <main+109>:  mov    eax,0x8048641
0x08048506 <main+114>:  mov    DWORD PTR [esp+0x4],edx
0x0804850a <main+118>:  mov    DWORD PTR [esp],eax
0x0804850d <main+121>:  call   0x80483ac <printf@plt>	    #print failure message
0x08048512 <main+126>:  leave
0x08048513 <main+127>:  ret
