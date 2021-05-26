# Input    : car
# Output : a

input_value = str(input("enter valid string :"))
# input_value = 'ab'

if len(input_value)%2 == 0:
    middle_index = int(len(input_value) / 2)
    print(input_value[middle_index-1:middle_index+1])
else:
    middle_index = int(len(input_value) / 2)
    print(input_value[middle_index])
