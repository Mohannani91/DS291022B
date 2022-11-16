numbers=(1,2,3,4,5,6,7,8,9,5,6,2,3,5,7,9,0)
even_count,odd_count=0,0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers in list:",even_count)
print("odd numbers in list:",odd_count)