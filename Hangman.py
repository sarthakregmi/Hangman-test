#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import sys


# In[81]:


word_to_guess='manakamana'
length=len(word_to_guess)
total_char=[]
length_round=round(0.3*length)
print('The length of string is',length)
ind= random.sample(range(0,length),length_round)
for i in ind:
    print('The character in index is{} is{}'.format(i,word_to_guess[i]))
display= length*'#'
for i in range(0,length):
    if i in ind:
        print(word_to_guess[i])
    else:
            print(display[i])
for i in range(0,length):
    if i in ind:
        char=word_to_guess[i]
        total_char.append(char)
print(total_char)


# In[52]:


unique=set(word_to_guess)
freq={}
for i in unique:
    a=word_to_guess.count(i)
    if a==1:
        continue
    freq[i]=a
freq_key=freq.keys()


# In[96]:


used_char=[]
find_var_index=[]
count=0
for i in range(0,15):
    guessed_char=input("Enter the character you guessed:\n")
    if guessed_char in word_to_guess:
        if guessed_char in used_char:
            print('you have already guessed the character')
            continue
        used_char.append(guessed_char)
        def charposition(str,char):
            position=[]
            for n in range(len(str)):
                if str[n]==char:
                    positon.append(n)
                return position
            find_var=charposition(word_to_guess,guessed_char)
            print(find_var)
            for i in range(0,length):
                if i in find_var:
                    print("The character in index is {} is{}".format(i,word_to_guess[i]))
                    total_char.append(word_to_guess[i])
                    find_var_index.append(i)
            for i in range(0,length):
                if i in find_var_index or i in ind:
                    print(given_name[i])
            else:
                    print(display[i])
    else:
        print("you couldn't guess the correct word!")
        count=count+1
        used_char.append(guessed_char)
        if(count==5):
            print('you couldn complete the game')
            break
print(total_char)
count_guessed=0
for i in range(0,length):
    if(word_to_guess[i] in total_char):
        count_guessed=count_guessed+1
        if(count_guessed==length and [freq[i]<total_char.count(i)for i in freq.key]):
            print('you have correctly guessed the word')
    sys.exit('you won!')
                                


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




