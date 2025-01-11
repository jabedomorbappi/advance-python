parent_list=[x for x in range(1,101)]
even_list=list(filter(lambda x:x%2==0,parent_list))
odd_list=list(filter(lambda x:x%2!=0, parent_list))
print(even_list)
print(odd_list)
