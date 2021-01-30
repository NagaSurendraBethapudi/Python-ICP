#program to find the wordcountin a file for each line and thenprint the output.
#Finally store the output back to the file.

from collections import Counter #using counter, we can count the key value pairs 
Notepad = open("input.txt", "r")
wordcounter = Counter(Notepad.read().split()) 
s2 = " "
for word in wordcounter.items(): 
    s1 = str(word)
    s2 = s1+s2
    print("{}:{}".format(*word))

#Storing the output back to input
Notepad = open("input.txt", "a") #opened the input with append mode
Notepad.write("\n")
Notepad.write(s2)

# # #Using another way
# Notepad = open("input.txt", "r")
# dic = dict()
# for line in Notepad:
#     line = line.lower().strip() #lowering and strip() method to lower the letters and removing the characters 
#     words = line.split(" ") #each line is sliced to words
#     for word in words:
#         if word in dic: #checking for samw word in dictonary
#             dic[word] = dic[word] + 1
#         else:
#             dic[word] = 1
# for key in list(dic.keys()):
#     print(key, ":", dic[key])
 
# #Storing the output back to input
# w = open("input.txt", "a") #opened the notepad wwith append mode
# w.write("Word count of above text is : ")
# for key in list(dic.keys()):
#     w.write("\n")
#     w.write(key)
#     w.write(":")
#     w.write(str(dic[key]))
# w.close()