# Importing array
import array as arr

# Array
array_num = arr.array('i',[1, 3, 5, 3, 7, 9, 3])
print("Original array : "+str(array_num))

# Checking the number of occurence of number 3
print("Number of occurence of the number 3 in the array : ",array_num.count(3))

# Reversing the digits
array_num.reverse()
print("Reverse the order of the items : ")
print(str(array_num))