# Input:” Hi how are you”
# Output : “you are how Hi”

input_value = str(input("enter valid string :"))
list1 = input_value.split(' ')
list1.reverse()
final_str = ' '.join(list1)
print(final_str)