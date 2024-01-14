            ############# Question no 3 #############

# 3} Write a Python program to square the elements of a list using map() function.
#   Sample List: [4, 5, 2, 9]
#   Square the elements of the list:
#   [16, 25, 4, 81]

def square_num(n):
  return n * n

Sample_list = [4, 5, 2, 9]
print("Original List: ",Sample_list)

result = map(square_num, Sample_list)
print("Square elements of the list:",list(result))