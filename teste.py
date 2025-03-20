a = int(input())
b = int(input())
c = int(input())

maior = (a + b + abs (a-b))/2
maiore = (a + c + abs (a-c))/2
final = maior + maiore + abs(maior-maiore)/2
print(final,'eh o maior')