#Function to check if number is prime
def prime(n):
    flag = 1
    if n == 2:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            flag = 0
            return False
        if flag == 1:
            return True

#Function to check number of prime Factors for a given number. 
def numberprimefactors(n):
    if prime(n):
         return 1
    count = 0
    for i in range(2, n // 2 + 1):
        if prime(i) and n % i == 0:
            count = count + 1
    return count 

numberprimefactors(n)



                
