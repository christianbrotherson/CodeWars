def manual_incrementing_matrix(num):
    list_of_lists = []
        
    for j in range(num): 
        loading_list = []
        for h in range(j, (j+num)): loading_list.append(h)
        list_of_lists.append(loading_list)
        
    return list_of_lists

print(manual_incrementing_matrix(5))

# def manual_incrementing_matrix(n):
#     matrix = [ [ None for y in range(n) ] for x in range(n) ]

#     counter = 0

#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix[idx][nested_idx] = counter + nested_idx
        
#         counter += 1

#     return matrix

# print(manual_incrementing_matrix(10))