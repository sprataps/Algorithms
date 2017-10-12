'''
Fibonacci sum till n
Print the nth fibonacci number
'''

def fibonacci_sum_recursive(n):
    if n==1:
        return 1
    if n==2:
        return 3
    return 1+(fibonacci_sum_recursive(n-1)+fibonacci_sum_recursive(n-2))

def fibonacci_number_recursive(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return fibonacci(n-1)+fibonacci(n-2)


#iterative fibonacci sum and number
def fibonacci_2(n):
    if n==1:
        return 1
    if n==2:
        return 2
    a,b=1,2
    sum=a
    for i in range(2,n):
        sum+=b
        temp=b
        b=a+b
        a=temp
    sum+=b
    print("Sum till n: "+str(sum))
    print("Nth Fibonacci number: "+str(b))

n=int(input("Enter the number: "))
fibonacci_2(n)
print("Recursive: "+str(fibonacci_sum_recursive(n)))
