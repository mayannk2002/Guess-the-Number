#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
randNumber = random.randint(1,100)


# In[2]:


guesses = 0
userGuess = None
while(userGuess != randNumber):
    userGuess = int(input("enter your Guess:"))
    guesses += 1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        print("you guessed it worng!")
        if(userGuess>randNumber):
            print("you guessed it worng! Enter a smaller number")
        else:
            print("you guessed it worng! Enter a larger number")
            
print(f"you guessed the number in {guesses} guesses")  


# In[ ]:




