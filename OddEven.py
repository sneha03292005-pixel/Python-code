#generating the odd and even program in different way;
#using for loop and range ect..
# for value in range(1,101):
#     if value % 3 == 0 and value % 5 == 0:
#         print("Fizz Bizz")
    
#     elif value % 3 == 0:
#         print("fizz")
#     elif value % 5 == 0:
#         print("Buzz")
    
#     else:
#         print(value)




def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False