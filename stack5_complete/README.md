# privilege escalation using shellcode

+ INT3(http://www.cs.columbia.edu/~junfeng/09sp-w4118/lectures/int3/int3.txt)
+ on examinig the code it is clear that it is simple code and just get the user input using the gets function
+ so what can we do with it
+ as like the challenge before all we need to do is to manipulate the return value after the execution of the main function
+ in such way that the instruction pointer goes to the stack pointer
+ (as we all know stack is something were we can store values and perform operation that's the reason why we need to set instrution pointer to the memory address of the stack pointer)
+ so check at which byte the segmentation fault occurs(using along string that follows a pattern)
+ and then replace the bytes(in my case T which starts at 73rd byte) with the memory address of the stackpointer
+ and then use INT3 to check whether the program enters into debugger mode if it enters then
+ just replace the INT3 instruction with the shellcode(you can use shell storm to find [shellcode](http://shell-storm.org/shellcode/files/shellcode-606.php))
+ and pipe the standard output of the exploit to the standard input of the program and most importantly remmember to get the standard input using a cat command inorder to get input from user to execute commands
+ *(python answerScript.py ; cat) | ./stack5*  
