print ("Lambda function in Python")

#Square number

square = lambda x: x**2

print(f"Square of 2: {square(2)}")
print(f"Square of 5: {square(5)}")

#Use of map() and lambda

numbers = [1,2,3,4]
squares = list(map(lambda x:x**2, numbers))

print(f"Squares of {numbers}: {squares}")

#Use of filter() and lambda

evens= list(filter(lambda x:x %2 ==0, numbers))

print(f"Even numbers of {numbers}: {evens}")

from os import system
if system("clear") != 0: system("cls")

#Use sorted() and  lambda
cars = [{"brand": "Toyota", "model": "Prius", "price" : 29000},
        {"brand": "BMW", "model": "X5", "price" : 85000},
        {"brand": "Seat", "model": "Ibiza", "price" : 21000},
        {"brand": "Audi", "model": "A3", "price" : 33000}]

cars_sorted = sorted(cars, key=lambda x: x["price"], reverse=True)
print(f"Cars sorted by price: {cars_sorted}")