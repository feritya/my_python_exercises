a = False
number=[1,2,3,4,5,6,7,8,5555]
alphabets=['a','b','c','d','e','f','y']

if a== True:
    print(max(number))
    #5555
if a== True:
    print(min(number))
    #1
if a== True:
    print(max(alphabets))
    #y
if a== True:
    print(min(alphabets))
    #a
if a== True:
    print(number[:3])
    #[1, 2, 3]
if a== True:
    print(number[::2])
    #[1, 3, 5, 7, 5555]
if a== True:
    print(alphabets[2:5])
    #['c', 'd', 'e']
if a== True:
    print(alphabets[::-1])
    #['y', 'f', 'e', 'd', 'c', 'b', 'a']

if a == True:
    number=number.insert(3,25)
    print(number)
    #[1,2,3,,25,4,5,6,7,8,5555]


if a== True:
    number.pop(2)
    print(number)
    #[1, 2, 4, 5, 6, 7, 8, 5555]
if a== True:
    number.remove(5555)
    print(number)
    #[1, 2, 4, 5, 6, 7, 8]
if a== True:
    number.sort()
    print(number)

    #[1,2,3,4,5,6,7,8,5555]
if a== False:
    alphabets.sort()
    print(alphabets)
    #['a','b','c','d','e','f','y']
if a== True:
    number.reverse()
    alphabets.reverse()
    print(number,alphabets)
    #[8, 7, 6, 5, 4, 2, 1] ['y', 'f', 'e', 'd', 'c', 'b', 'a']
if a==True:
    print(number.count(5))
    print(alphabets.count('a'))
    #1
    #1

if a == False:
    number.clear()
    print(number)
    #[]


