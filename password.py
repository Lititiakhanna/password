#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

words=input("Enter the words: ")
word=words.replace(" ","")

max_len=15

input_words=list(word)
rand_words=random.choice(input_words)

for x in range(max_len-1):
    rand_words=rand_words+random.choice(input_words)

rand_words_list=list(rand_words)
random.shuffle(rand_words_list)
sug_pass="".join(rand_words_list)

print(sug_pass)
f=open("pass.txt","a")
f.write("Entered words by the user are "+words+". Suggested password is "+sug_pass+"\n")
f.close()

digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
locase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upcase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '_', '+', '!', '&', '[', ']', '-']

password=input("Enter a password(atleast 8 characters)")
pass_list=[]
for i in password:
    if(i in digits):
        pass_list.append('d')
    elif(i in locase):
        pass_list.append('l')
    elif(i in upcase):
        pass_list.append('u')
    elif(i in symbols):
        pass_list.append('s')
    else:
        pass_list.append('o')
pass_list=set(pass_list)
pass_list=list(pass_list)
final_list=sorted(pass_list)

if(len(password)>=8):
    if(final_list==['d', 'l', 'o', 's', 'u'] or final_list==['d', 'l', 's', 'u']):
        print('Password entered is strong')
    else:
        print('Password entered is weak')
else:
    print("Enter atleast 8 characters")


# In[ ]:




