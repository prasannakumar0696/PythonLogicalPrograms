# Input : 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

input_value = int(input("enter valid single integer :"))
dict1 = {}
for i in range(1, input_value+1):
    dict1[i] = i*i
print(dict1)

dict2 = {i: i*i for i in range(1, input_value+1)}
print(dict2)
