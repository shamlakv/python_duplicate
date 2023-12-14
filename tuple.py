original_tuple=(1,2,3,4,5)
converted_list=list(original_tuple)
converted_list[2]=6
converted_list.append(7)
new_tuple=tuple(converted_list)
print("original tuple",original_tuple)
print("modified tuple",new_tuple)
