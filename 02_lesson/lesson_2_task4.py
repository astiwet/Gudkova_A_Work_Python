
def fizz_buzz(n):
    for i in range(1, n):
        if (i % 3 == 0) and (i % 5 == 0):
           print("Fizz_Buzz")
        elif i % 5 == 0:
           print("Buzz")
        elif (i % 3 == 0):
           print("Fizz")
        else: 
           print(i)
        
number = input("введите число")
num = int(number)
fizz_buzz(num)
