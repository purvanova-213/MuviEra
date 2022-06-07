print("-"*25,'CHECKSUM ERROR DETECTION MECHANISM',25*'-')
print("\n",25*"-","At Sender's Side","-"*25,"\n")
data_bits = input('Enter the Data Bits : ')
checksum_bits = int(input("Enter number of checksum bits: "))
sum="0"
sum = int(sum,2)
for i in range(0, len(data_bits), checksum_bits):
    part_i = data_bits[i: i + checksum_bits]
    print("The Data Part : ",part_i)
    part = int(part_i,2)
    sum = sum+part
binary_sum = bin(sum)
print(binary_sum)
finalsum = binary_sum[2:]
if len(finalsum)==checksum_bits:
    finalsum = finalsum
else:
    finalsum = binary_sum[3:]

#normal binary string s saved in list
def Convert(string):
   list1=[]
   list1[:0]=string
   return list1
final_sum = Convert(finalsum)
print(final_sum)
def complement(s):
    for i in range (0,len(s)):
        if s[i] == '1':
            s[i] = '0'
        else:
            s[i] = '1'
complement(final_sum)
print(final_sum)
#List is changed to string binary
def convert(s):
    checksum = ""
    return (checksum.join(s))
checksum = convert(final_sum)
print("The Checksum Calculated is: ",checksum)
codeword = data_bits + checksum
print('The Transmitter sequence will be: ',codeword)
print("\n",25*"-","At Receiver's Side","-"*25,"\n")
data_bits1 = input('Enter the Data Bits : ')
checksum_bits1 = int(input("Enter number of checksum bits: "))
sum1="0"
sum1 = int(sum1,2)
for i in range(0, len(data_bits1), checksum_bits1):
    part = data_bits1[i: i + checksum_bits1]
    parts = int(part,2)
    print("The Data Part: ",part)
    sum1 = sum1+parts
binarysum = bin(sum1)
finalsum1 = binarysum[2:]
if len(finalsum1)==checksum_bits1:
    finalsum1 = finalsum1
else:
    finalsum1 = binarysum[3:]
final_sum1 = Convert(finalsum1)
complement(final_sum1)
value = convert(final_sum1)
print("The Computed Received Sequence: ",value)
if final_sum1.count('1')>0:
    print("This is an Errored Message...Please try Transmitting the Message again.")
else:
    print("The Transmitted Sequence was Received Successfully with no Error Present.")
print("\n",30*"-","DONE","-"*30,"\n")




