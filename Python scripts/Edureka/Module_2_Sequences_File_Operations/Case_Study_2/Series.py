# By Gaurav
# Program for 1 / 2 + 2 / 3 + 3 / 4 + ... + n / n + 1

n = int(input("Enter a number greater than zero : "))
m = 0
j = 1
for i in range (1,n+1):
    m= m+(j/(j+1))
    j+=1

print(m)