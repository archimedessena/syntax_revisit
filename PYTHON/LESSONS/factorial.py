# Write a function to calculate the factorial of a number 

def factorial_function(s):
    result = 1  
    for i in range(2, s+1):
        result *= i
    return result
        


print(factorial_function(8))