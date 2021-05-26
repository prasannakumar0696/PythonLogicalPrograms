# Input: ' how are you, 123 !!!'
# Output: letters = 9 ,digits = 3

input_value = str(input("enter valid string :"))
# input_value =' how are you, 123 !!!'
letters, digits = 0, 0
for i in input_value:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("letters = ", letters, "digits = ", digits )