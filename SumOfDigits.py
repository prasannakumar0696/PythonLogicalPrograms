# Input: 161
# Output: 8

input_value = int(input("enter valid integer :"))
output_value = 0
# scenario 1
for i in str(input_value):
    output_value = output_value + int(i)
print(output_value)

# scenario 2
# output_value1 = 0
# while input_value!=0:
#     last = int(input_value%10)
#     output_value1 += last
#     input_value /= 10
#
# print(output_value1)