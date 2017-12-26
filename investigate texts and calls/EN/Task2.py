"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""

#Create dictionary for duration of each telephone number in calls, and return the list of max value
def duration(lists):
    phone_number_duration_dic = {}
    max_dic = []
    for number in range(len(lists)):
        #For calling numbers, sum up total duration times of each
        if lists[number][0] not in phone_number_duration_dic:
            phone_number_duration_dic[lists[number][0]] = int(lists[number][3])
        else:
            phone_number_duration_dic[lists[number][0]] += int(lists[number][3])
        #For receiving numbers, sum up total duration times of each
        if lists[number][1] not in phone_number_duration_dic:
            phone_number_duration_dic[lists[number][1]] = int(lists[number][3])
        else:
            phone_number_duration_dic[lists[number][1]] += int(lists[number][3])
    #print(phone_number_duration_dic)   #Test result
    #print(len(phone_number_duration_dic))  #Double check the length with Task1
    #Reverse values and keys of dictionary, in order to use max() finding out the longest time
    max_dic = max(zip(phone_number_duration_dic.values(),phone_number_duration_dic.keys()))
    return max_dic

target_phone_number = duration(calls)[1]
target_duration_time = duration(calls)[0]
print("<{}> spent the longest time, <{}> seconds, on the phone during September 2016.".format(target_phone_number, target_duration_time))
