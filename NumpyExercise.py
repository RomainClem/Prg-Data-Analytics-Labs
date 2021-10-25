import numpy as np


# arr = np.zeros((12, 3), dtype=int)

# arr2 = arr.reshape((6, 6))

# print(arr2)

# data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')

# resultMaxArr = np.amax(data, axis=0)
# resultMinArr = np.amin(data, axis=0)
# resultMeanArr = np.mean(data, axis=0)

# print ("Maximum Results")
# print ("\t Casual Users", resultMaxArr[13])
# print ("\t Registered Users", resultMaxArr[14])

# print ("Minimum Results")
# print ("\t Casual Users", resultMinArr[13])
# print ("\t Registered Users", resultMinArr[14])

# print ("Mean Results")
# print ("\t Casual Users", resultMeanArr[13])
# print ("\t Registered Users", resultMeanArr[14])

# arr2D = np.array([[45, 3, 67, 34],[12, 43, 73, 36]], float)
# boolArr3 = np.array([True, False], bool)
# print (arr2D[boolArr3])

# result = data[:, 13] > data[:, 14]

# print ("Percentage of time where casual users > registered ",  (len(data[result])*100.0)/len(data))


data = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7], [6, 2, 3]], float)

# a, b, c = np.array_split(data, 3)

# print(a)
# print(b)
# print(c)

# a = np.transpose(data)
# print(data)
# print(a)

# a = np.array([[10,40],[30,20]])
# print("Original array:")
# print(a)
# print("Sort the array along the first axis:")
# print(np.sort(a, axis=0))
# print("Sort the array along the last axis:")
# print(np.sort(a))
# print("Sort the flattened array:")
# print(np.sort(a, axis=None))



# data_type= [('name', 'S4'), ('class', int), ('height', float)]
# students_details= [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# # create a structured array
# students = np.array(students_details, dtype=data_type)   
# print("Original array:")
# print(students)
# print("Sort by height")
# print(np.sort(students, order='height'))  
# print(students[0]['name'])

# x = np.array(['python', 'PHP', 'java', 'C++'], dtype='str')
# print("Original Array:")
# print(x)
# capitalized_case= np.char.capitalize(x)
# lowered_case= np.char.lower(x)
# uppered_case= np.char.upper(x)
# swapcased_case= np.char.swapcase(x)
# titlecased_case= np.char.title(x)
# print("\nCapitalized: ", capitalized_case)
# print("Lowered: ", lowered_case)
# print("Uppered: ", uppered_case)
# print("Swapcased: ", swapcased_case)
# print("Titlecased: ", titlecased_case)

# print("March, 2017")
# print(np.arange('2017-03', '2017-04', dtype='datetime64[D]'))

yesterday = np.datetime64('today', 'D') -np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)