"""
Intro to Python Lab 1, Task 3

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


#Create a dictionary that includes all phone numbers called by (080) and related times
def phone_number_filter(lists):
    phone_called_dic = {}
    for item in lists:
        if '(080)' in item[0]:
            if item[1] in phone_called_dic:
                phone_called_dic[item[1]] += 1
            else:
                phone_called_dic[item[1]] = 1
    #print(phone_called_dic)     #Check the result of the dictionary
    return phone_called_dic

all_numbers_called_dic = phone_number_filter(calls)
all_numbers_called_list = []       #Put all numbers called by (080)
target_number_list = []            #Put target numbers called by (080)
code_list = []                     #Put target codes called by (080)
n = 4                              #4 digits for mobile phone code

all_numbers_called_list = sorted(all_numbers_called_dic.keys())
#print(all_numbers_called_list)    #Check the result of the list

#Get target numbers called by (080)
for item in all_numbers_called_list:
    if item[:2] == '(0' or item[0] == '7' or item[0] == '8' or item[0] == '9':
        target_number_list.append(item)

#Get target codes called by (080)
for item in target_number_list:
    for number in range(len(item)):
        if item[number] == ')':
            code_list.append(item[:(number+1)])
    if item[0] == '7' or item[0] == '8' or item[0] == '9':
        code_list.append(item[:n])
code_list = '\n'.join(sorted(list(set(code_list))))

print("The numbers called by people in Bangalore have codes: \n{}".format(code_list))

target_called_times = 0
#Get how many times (080) were called by (080)
for key in all_numbers_called_dic.keys():
    if '(080)' in key:
        target_called_times += all_numbers_called_dic[key]
#print(target_called_times)       #Check the result
total_called_tmies = sum(all_numbers_called_dic.values())    #Get how many times all numbers were called by (080)
print(total_called_tmies)         #Check the result
percentage = target_called_times/total_called_tmies
#print(percentage)     #Check the final result
print("<{}> percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format('%.2f%%' % (percentage * 100)))
