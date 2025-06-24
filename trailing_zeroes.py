def factorial(n):
    if n==0 or n==1:    # base case
        return 1
    else:
        return n*factorial(n-1)   # recursively calling func again

def trailingZeros(n):   
    # count=0                           # One way
    # while (fact%10==0):
    #     count+=1
    #     fact=fact//10
    # return count
    i=5
    count=0
    while(n//i !=0):                    # The Better way around for easier computation by using number theory
        count=count+int(n/i) 
        i=i*5
    return count 

if __name__=="__main__":   # entry point of the program and prevents accidental code execution on import
    n=int(input("Enter number to get the factorial of: "))                             
    fact=factorial(n)
    print("Factorial is: ", fact)
   
    print("Trailing Zeroes: ",trailingZeros(n))   
