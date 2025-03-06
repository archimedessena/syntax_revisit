my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def extra_check():
    num = input("enter a number: ")
    if num in my_list:
        print(num, "is available")
    else:
        print(num, "is not available")
    return num


check = extra_check()
print(check)