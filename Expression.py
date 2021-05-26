input_value = input("enter valid Special Chars: ")


def check_expr(val):
    if len(input_value)%2 == 0:
        for i in range(int(len(input_value)/2)):
            if input_value[i] == '(' and input_value[-(i+1)] == ')':
                continue
            elif input_value[i] == '{' and input_value[-(i+1)] == '}':
                continue
            elif input_value[i] == '[' and input_value[-(i+1)] == ']':
                continue
            else:
                return "Invalid expression"
        return "equally balanced"
    else:
        return "unequally balanced"


print(check_expr(input_value))