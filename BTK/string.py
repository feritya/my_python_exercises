i = "   hello there,my name is ferit"

print(i.lower())
#    hello there,my name is ferit
print(i.upper())
#   HELLO THERE,MY NAME IS FERIT
print(i.title())
#   Hello There,My Name Is Ferit
print(i.capitalize())
#   hello there,my name is ferit
print(i.strip())
#hello there,my name is ferit
print(i.split())
#['hello', 'there,my', 'name', 'is', 'ferit']
print(i.split()[0])
#hello
print(i.split(','))
#['   hello there', 'my name is ferit']
a=False
if a==True:
    i=i.split()
    print('*'.join(i))
#hello*there,my*name*is*ferit
print(i.find('t'))
#9
print(i.strip().startswith('h'))
#True
print(i.startswith('h'))
#False
print(i.endswith('t'))
#True
print(i.replace( ' ','/'))
#///hello/there,my/name/is/ferit
print(i.center(20))
#   hello there,my name is ferit