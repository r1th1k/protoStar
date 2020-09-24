# it is similiar to stack6 except instead of checking for b7* it  know check for b*

+ so we cannnot able  to access anything from .data section(it contains all the variables)
+ but we can return to a ret instruction from the .text section(it contains the instruction or code) and then from there we can use ret2libc exploit
+ you can find the ret instruction using objdump or you can use the address of ret instruction in the getpath or main function 
+ and everything after that are similiar to stack6
