# #Reverse List :
# my_list = [10 , 20 , 30 , 40 , 50 , 11]
# print(my_list[-1: : -1])


# ## Common Elements :
# list1 = [1 , 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# empty_list = []
# for i in list1  :
#     if i == 4 and 5 :
#         for j in list2 :
#             if j< 6 :
#                 empty_list.append(i and j)
# print(empty_list)

# # Unique Elements :
# original_list = [1 , 2 , 2 , 3 , 4 , 4 , 5]
# unique_list = []
# for i in original_list :
#     if i not in unique_list :
#         unique_list.append(i)
# print(unique_list)

# #Remove Duplicates:
# duplicate_list = [1 , 2 , 2 , 3 , 4 , 4 , 5]
# original_list = []
# for i in duplicate_list :
#     if i not in original_list :
#         original_list.append(i)
# print(original_list)

# ##Exercise 1 : List Concatenation
# print([i for i in [1 , 2 , 3 , 4 , 5] + [6 , 7 , 8 , 9 , 10]])

# # Exercise 2 : List Repetition
# print([i for i in[[1 , 2 , 3] ,  [1 , 2 , 3] , [1, 2 , 3]]])

# #Exercise 3 : List Removal
# print([i for i in [1 , 2 , 3 , 4 , 5] if  i %2 != 0])

# #Exercise 4 : List Insertion
# print([i for i in [10 , 11 , 12] + [20 , 30 , 40]])

# ##List comprehensions
# ##square Numbers
# print([i**2 for i in [1,2,3,4,5,6,7,8,9,10]])

# #Even Numbers
# print([i for i in range(1 , 21)if i%2 == 0])

# #Words Lengths
# print([len(i) for i in  ["apple" , "banana" , "cherry" , "date"]])



