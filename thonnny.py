import os
import random
print(os.path.exists("C:\\Users\\hazel\\Documents\\thonny\\names.txt"))
my_list=[]
with open("C:\\Users\\hazel\\Documents\\thonny\\names.txt", "r") as my_file:
    for line in my_file:
        print(line.strip())
        my_list.append(line.strip())
        cpu_choice = random.choice(my_list)
        print (cpu_choice)


"""
my_list = []
my_list.append(1)
my_list.append(17)
print (my_list)
my_list.append(420692)
print (my_list)
print(my_list[-1])

print(len(my_list))
"""

my_list.append(line)
print (my_list)
print(len(my_list))