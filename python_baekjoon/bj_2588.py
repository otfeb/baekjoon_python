a = int(input())
b = int(input())

one = b%10
ten = b%100//10
hundred = b//100

print(a*one, a*ten, a*hundred, a*b, sep='\n')
