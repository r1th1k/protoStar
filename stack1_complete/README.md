# stack1

on examinig the code from the website it is clear that cracking the program is not a big deal as it  is the 

same program as before except with a little changes (i.e)it check for the given number of argument and 

the value for the modified variable is to be set as `0x61626364`(abcd as hex) in order to crack the program.

And the other thing to note is it is based on little endian system so the most significant bit go to the 

higher memory address and the least singnificant bit goes to the lower memmory address.

So as before we need to give 64 characters but now as an argument

**64characters(since the buffer is 64)+(abcd in reverse order because of the little endian)** 
