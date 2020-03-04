#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# ## Defining Bot

# In[2]:


bot=ChatBot("ZEMAC")
bot.set_trainer(ChatterBotCorpusTrainer)


# ### Training Chatbot

# In[3]:


bot.train("chatterbot.corpus.english")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


while(1):
    message=input("You:")
    if(message=="Bye"or message=="bye"):
        print("{} : See you later".format(bot.name))
        break
    if(message!="Bye" or message!="bye"):       
        reply=bot.get_response(message)
        print("{}: {}".format(bot.name,reply))


# In[ ]:





# In[ ]:





# In[ ]:




