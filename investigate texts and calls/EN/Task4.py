"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
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

flat_texts = flat(texts)
flat_calls = flat(calls)
#print(flat_texts[:7])            #Check the result
#print(flat_calls[:10])           #Check the result

#Delete timestamp of text message, so only telephone numbers left
def phone_number_texts(lists):
    temp_list1 = []
    for number in range(len(lists)):
        if (number+1) % 3 == 0:              #Search timestamp elements in texts
            temp_list1.append(lists[number])
    #print(temp_list1[:5])       #Check the result
    for item in temp_list1:
        if item in lists:
            lists.remove(item)          #Delete timestamp elements in texts
    #print(lists[:7])            #Check the result
    #print(len(lists))           #Check the result
    return lists
x = phone_number_texts(flat_texts)
#print(len(x))                   #Check the result
#print(x[:7])                    #Check the result

#Delete timestamp and duration of calls, so only telephone numbers left
def phone_number_calls(lists):
    temp_list2 = []
    temp_list3 = []
    for number in range(len(lists)):
        if (number+1) % 4 == 0:         #Search duration elements in calls
            temp_list2.append(lists[number])
    #print(temp_list[:5])        #Check the result
    for item in temp_list2:
        if item in lists:
            lists.remove(item)         #Delete duration elements in calls
    #print(temp_list2[:8])       #Check the result
    for number in range(len(lists)):
        if (number+1) % 3 == 0:        #Search timestamp elements in calls
            temp_list3.append(lists[number])
    #print(temp_list[:5])        #Check the result
    for item in temp_list3:
        if item in lists:
            lists.remove(item)        #Delete timestamp elements in calls
    #print(lists[:7])            #Check the result
    #print(len(lists))           #Check the result
    return lists
y = phone_number_calls(flat_calls)
#print(len(y))                   #Check the result
#print(y[:10])                   #Check the result

set_number_texts = set(x)          #Create set of all numbers in texts

outgoing_calls_list = []
receiving_calls_list = []
#Create outgoing calls list and receiving calls list from calls.csv
for number in range(len(y)):
    if number % 2 == 0:
        outgoing_calls_list.append(y[number])
    else:
        receiving_calls_list.append(y[number])

#print(outgoing_calls_list[:3])      #Check the result
#print(receiving_calls_list[:3])     #Check the result

outgoing_calls_set = set(outgoing_calls_list)
receiving_calls_set = set(receiving_calls_list)

set_number_texts_rcvcalls = set_number_texts | receiving_calls_set     #Create aggregate set of two sets
#print(set_number_texts_rcvcalls)    #Check the result

telemarketers = []
#Outgoing calls from telemarketers might be not in phone number sets of texts.csv and receiving calls
for item in outgoing_calls_set:
    if item not in set_number_texts_rcvcalls:
        telemarketers.append(item)
print("These numbers could be telemarketers: \n{}".format('\n'.join(sorted(list(telemarketers)))))
