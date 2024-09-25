number = int(input("Stick in number"))
number2 = int(input("Stick in number"))
common=[]
def find_factors(number,number2):
    for i in range(1,number+1):
        if number % i == 0 and number2 % i == 0:
            common.append(i)
find_factors(number, number2)
print(common[-1])
