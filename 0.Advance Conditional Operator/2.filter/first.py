def even(num):
    return num%2==0 

a_list=[1,2,3,4]

b=filter(even,a_list)
print(list(b))