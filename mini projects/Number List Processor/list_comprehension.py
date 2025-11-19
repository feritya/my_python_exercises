sayilar=[]
cift_sayilar=[]

for i in range(0,101):
    sayilar.append(i)

cift_sayilar=[x for x in  sayilar if x%2==0]
uclu_sayilar=[x for x in sayilar if x%3==0]
guclu_sayilar=[x for x in sayilar if x%2==0 if  x%3==0]
sum_cift_uclu =sum([ x for x in sayilar if x%3==0 or x % 2==0 ])
average_cift_uclu =sum([ x for x in sayilar if x%3==0 or x % 2==0 ])/len([ x for x in sayilar if x%3==0 or x %2==0])
asal_sayilar=[x for x in sayilar  if x>1 and all(x% i !=0 for i in range(2,x) )]
print()