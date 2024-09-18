# x = 3
# y = float(3)
# print(x,y)
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)
#     print(values[0])
# print(values[6])
# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)
# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
#     print(f"Congrats it is {day_of_week}")
# else:
#     print("incorrect")
#     x = "test"
#     print(f"IT IS NOT {day_of_week}")
# odd_or_even = int(input("Input number"))
# if (odd_or_even %2) == 0:
#     print("even")
# else:
#     print("odd")
# Service = input("Rate you serice, bad, okay, good, great, ")
# bill = int(5)
# if Service == "bad":
#     print(bill)
# if Service == "okay":
#     print(bill*1.15)
# if Service == "good":
#     print(bill*1.2)
# if Service == "great":
#     print(bill*1.25)
number = int(input("Stick in number"))

def find_factors(x):
    factors = []
    for i in range (1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors
factors= find_factors(number)
print(factors)

