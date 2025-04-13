print ("List Comprehension in Python")

# Print square numbers between 1 and 10

square_numbers = [ number**2 for number in range(1,11) ]

print(f'Square numbers between 1 and 10: {square_numbers}')

# Print even numbers between 1 and 10

even_numbers = [ number for number in range(1,11) if number % 2 ==0 ]

print(f'Even numbers between 1 and 10: {even_numbers}')

# Nested loop

adjectives = ["Tasty", "Big", "Cheap" ]
fruits = ["watermelon", "pineaple", "berry"]

combination = [ (adjetive , fruit) for adjetive in adjectives for fruit in fruits ]

print(combination)

# Flatten a matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

flat_matrix = [ num for row in matrix for num in row ]

print(f"Flatten matrix: {flat_matrix}")

# 3x3 identity matrix
size = 5
identity_matrix = [[1 if i==j else 0 for j in range(size)] for i in range(size)]

print(f"Identity matrix of size: {size}:\n {identity_matrix}")