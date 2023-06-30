#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[3]:


header = {"User-Agent":"Crome"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[4]:


html.status


# In[5]:


obj = bs(html)


# In[6]:


newCases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]


# In[7]:


deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# In[8]:


notifier = ToastNotifier()
message = "New Cases - " + newCases + "\nDeath - " + deaths


# In[9]:


message


# In[10]:


notifier.show_toast(title="COVID-19 Update", msg=message, duration=5)


# In[ ]:





# In[ ]:




