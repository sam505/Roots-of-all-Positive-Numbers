number = input("Enter the number to get the square root: ")
root = input("Enter the root you want to get: ")
number = int(number)
root = int(root)
estimate = 0
solution = 1
solution_one = 1

while (solution <= 0 and solution_one <= 0) or (solution >= 0 and solution_one >= 0):
    estimate += 1
    solution = ((estimate**root) - number)
    solution_one = (((estimate + 1)**root) - number)
    if solution == 0:
        break

print("Estimate used is: " + str(estimate))

soln = (estimate**root) - number
soln_one = root*(estimate**(root-1))
square_root_one = estimate
square_root = estimate - (soln/soln_one)
square_root = round(square_root, 10)
square_root_one = round(square_root_one, 10)

while square_root != square_root_one:
    square_root_one = square_root
    soln = (square_root ** root) - number
    soln_one = root*(square_root_one**(root-1))
    square_root = square_root - (soln / soln_one)
    square_root = round(square_root, 10)
    print (square_root)


print("The square root is: " + str(square_root))
