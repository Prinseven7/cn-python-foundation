"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""

#Flatten texts and calls into one dimentional lists
def flat(two_dimention_lists):
    one_demention_list = []
    for item in two_dimention_lists:
        if isinstance(item, list):
            one_demention_list.extend(flat(item))
        else:
            one_demention_list.append(item)
    return one_demention_list

flat_texts = []
flat_calls =[]
flat_texts = flat(texts)
flat_calls = flat(calls)
#print(flat_texts[:7])        #Check the result
#print(flat_calls[:10])       #Check the result

#Delete timestamp of text message, so only telephone numbers left
def phone_number_texts(lists):
    temp_list1 = []
    for number in range(len(lists)):
        if (number+1) % 3 == 0:              #Search timestamp elements in texts
            temp_list1.append(lists[number])
    #print(temp_list1[:5])    #Check the result
    for item in temp_list1:
        if item in lists:
            lists.remove(item)          #Delete timestamp elements in texts
    #print(lists[:7])         #Check the result
    #print(len(lists))        #Check the result
    return lists
x = phone_number_texts(flat_texts)
#print(len(x))                #Check the result
#print(x[:7])                 #Check the result

#Delete timestamp and duration of calls, so only telephone numbers left
def phone_number_calls(lists):
    temp_list2 = []
    temp_list3 = []
    for number in range(len(lists)):
        if (number+1) % 4 == 0:         #Search duration elements in calls
            temp_list2.append(lists[number])
    #print(temp_list[:5])     #Check the result
    for item in temp_list2:
        if item in lists:
            lists.remove(item)         #Delete duration elements in calls
    #print(temp_list2[:8])    #Check the result
    for number in range(len(lists)):
        if (number+1) % 3 == 0:        #Search timestamp elements in calls
            temp_list3.append(lists[number])
    #print(temp_list[:5])     #Check the result
    for item in temp_list3:
        if item in lists:
            lists.remove(item)        #Delete timestamp elements in calls
    #print(lists[:7])         #Check the result
    #print(len(lists))        #Check the result
    return lists
y = phone_number_calls(flat_calls)
#print(len(y))                #Check the result
#print(y[:10])                #Check the result

set_number_texts = set(x)          #Create set of all numbers in texts
set_number_calls = set(y)          #Create set of all numbers in calls
#print(len(set_number_calls)) #Check the result
set_number_texts_calls = set_number_texts | set_number_calls     #Create aggregate set of two sets

print("There are <{}> different telephone numbers in the records.".format(len(set_number_texts_calls)))
