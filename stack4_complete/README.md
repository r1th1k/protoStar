# for this challenge you need to know about the structure of stack
+ so as we know the stackframe is space between the basepointer and stackpointer and it is used to store local variables and perform operations
+ so after the variable the base pointer is present
+ and after the base pointer the return address to the next instruction will be present
+ so if we could change the return address then we could redirect the instruction pointer to the desired location or memory address
+ inorder to find the byte at which the return address changes one can use patterns to identify them
+ so if you run the program with that input u will get a segmentation fault error with the <value>
+ so u can remove that specific value and replace it with the required memory address of the function
 
