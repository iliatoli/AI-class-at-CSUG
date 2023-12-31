list1 = []
n1 = 0
while n1 > 10 or n1 < 1:
    n1 = int(input('Please enter the number of elements of list A between 0 and 11: '))

for i in range(n1):
    add = int(input('Please enter a number: '))
    list1.append(add)

list2 = []
n2 = 0
while n2 > 10 or n2 < 1:
    n2 = int(input('Please enter the number of elements of list B between 0 and 11: '))

for i in range(n2):
    add = int(input('Please enter a number: '))
    list2.append(add)

def cartesian_product(lst1, lst2):
    result = []
    for x in lst1:
        for y in lst2:
            result.append((x,y))
    return result

print('The Cartesian product of the two lists is:')
print('AxB = ', end = '')
print(cartesian_product(list1,list2))
