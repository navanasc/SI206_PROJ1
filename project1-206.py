import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	# get a list of dictionary objects from the file
	#Input: file name
	#Ouput: return a list of dictionary objects where
	#the keys are from the first row in the data. and the values are each of the other rows

	#Open file for reading.
	inFile = open(file, "r")

	#First line is going to contain all of the keys needed to construct dictionaries.
	line = inFile.readline()
	# Strip newline character
	line = line.strip("\n")
	#Split at ',' to get a list of keys, save them in a list to be re-used to each dictionary.
	keys_list = line.split(',')
	#Create an empty list to carry all the dictionaries that will be constructed from rows of values.
	dicts_list = []
	#Get the next line. While there is a next line, keep looping.
	line = inFile.readline()
	# Strip newline character
	line = line.strip("\n")
	#Create a loop.
	while line:
		#Create a dictionary that will hold the values from line with keys from keys_list.
		values_dict = {}
		#Split line into values at comma.
		values = line.split(',')
		#Assign values to the correct keys.
		for i in range(len(keys_list)):
			values_dict[keys_list[i]] = values[i]
		#Append to dictionary list.
		dicts_list.append(values_dict)
		#Read next line to update condition of the while loop.
		line = inFile.readline()
		# Strip newline character
		line = line.strip("\n")
	#Close file.
	inFile.close()
	#Return list of dictionary objects.
	return dicts_list

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	#Sort the list based on key col using lambda temporary function.
	#Make sure col is a string.
	col = str(col)
	#Note: x is the individual dictionaries in the list of dictionary objects data.
	sorted_data = sorted(data, key = lambda x: (x[col]))
	#Create a return string that will contain firstName and lastName of the first item in the sorted list.
	ret_string = sorted_data[0]["First"] + " " + sorted_data[0]["Last"]
	#Return the return string.
	return ret_string


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	#Create variables to keep count of instances of each class standing.
	freshman_count = 0
	sophomore_count = 0
	junior_count = 0
	senior_count = 0
	#Traverse the list of dictionaries, access each dict with key "Class."
	#Count instances of each class standing with if statments.
	for person_dict in data:
		if person_dict["Class"] == "Freshman":
			freshman_count += 1
		elif person_dict["Class"] == "Sophomore":
			sophomore_count += 1
		elif person_dict["Class"] == "Junior":
			junior_count += 1
		elif person_dict["Class"] == "Senior":
			senior_count += 1
	#Create a list of all (Class, count) tuples, and sort in descending order.
	tup_list = [("Freshman", freshman_count), ("Sophomore", sophomore_count), ("Junior", junior_count), ("Senior", senior_count)]
	sorted_list = sorted(tup_list, key = lambda x: x[1], reverse = True)
	#Return sorted list.
	return sorted_list


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	#Create a dictionary to hold all the months in a year and their respective counts.
	months_dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0}
	#Traverse the list of dictionaries, access with key "DOB"
	for person_dict in a:
		#Within each DOB, split at "/", and the first value will be the month.
		DOB_vals = person_dict["DOB"].split("/")
		month = str(DOB_vals[0])
		#Use the month number as the key to access months_dict, and update count.
		months_dict[month] += 1
	#Sort month dictionary by count, and return the month with the highest count.
	#dictionary items() method will give a list of pair of tuples that can be sorted.
	sorted_months_list = sorted(months_dict.items(), key = lambda x: x[1], reverse = True)
	#Return the highest-count month number as integer.
	return int(sorted_months_list[0][0])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	#Read fileName for writing output.
	outFile = open(fileName, "w")
	#Sort the list based on key col using lambda temporary function.
	#Make sure col is a string.
	col = str(col)
	#Note: x is the individual dictionaries in the list of dictionary objects a.
	sorted_dicts_list = sorted(a, key = lambda x: (x[col]))
	for item in sorted_dicts_list:
		#Get first name, last name, and email for writing output.
		first = item["First"]
		last = item["Last"]
		email = item["Email"]
		#Write output into outfile in the correct format.
		outFile.write(first + ',' + last + ',' + email + '\n')
	#Close file.
	outFile.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	
	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
