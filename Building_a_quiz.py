import random


questions = [
    "What color are apples?\n(a) Red/Green\n(b) Yellow\n(c) Blue\n",
    "What color are bananas?\n(a) Red/Green\n(b) Yellow\n(c) Blue\n",
    "What color are oranges?\n(a) Red/Green\n(b) Yellow\n(c)Oranges\n",

]
count = 0

response1 = input(questions[0]).lower()
if response1 == 'a' or response1 =='A':
    print(response1 + " Is correct.")
    count+=1
else:
    print(response1 + " Is not correct")

response2 = input(questions[1]).lower()
if response2 == 'b' or response2 =='B':
    print(response2 + " Is correct.")
    count+=1
else:
    print(response2 + " Is not correct")

response3 = input(questions[2]).lower()
if response3 == 'c' or response3 =='C':
    print(response3 + " Is correct.")
    count+=1
else:
    print(response3 + " Is not correct")
    

#print(random.choice(questions))

grade = count/3
grade_percent = "{:.0%}".format(grade)

print(f"You correctly answered {count} questions.")
print(f"You scored a {grade_percent}")



