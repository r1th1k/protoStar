# this challenge is basically based on changing the instruction pointer to with the desired memory address inorder to go to that specific memory address

+ first identify the memory address of win() function
+ then open the program in gdb
+ give the memory address as the input after 64 chars since the buffer is 64 and fp in stored after the buffer in stack
+ write a python exploit and store it in the tmp and save the result in file
+ and while running the program use the symbol "<" inorder to redirect the contents of the file as an input

* tha exploit is found in the answerScript

