def print_squares_of_numbers_upto(n):
    for i in range(1,n+1):
        print(i*i)

#print_squares_of_numbers_upto(10)

def print_squares_of_even_numbers_upto(n):
    for i in range(2,n+1,2):
        print(i*i)

# print_squares_of_even_numbers_upto(10)

def print_squares_in_reverse(n):
    for i in range(n,0,-1):
        print(i)

print_squares_in_reverse(10)