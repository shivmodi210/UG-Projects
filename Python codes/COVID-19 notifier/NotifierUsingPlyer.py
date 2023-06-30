#!/usr/bin/env python
# coding: utf-8

# In[9]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from plyer import notification
import time


# In[10]:


header = {"User-Agent":"Crome"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)

obj = bs(html)
newCases = obj.find("li", {"class":"news_li"}).strong.text.split()[0] 

deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

msg = "New Cases - " + newCases + "\nDeath - " + deaths


# In[11]:


if __name__=="__main__": 
  
        notification.notify( 
            title = "COVID-19 Update", 
            message= msg , 
            
            # displaying time 
            timeout=2)
        # waiting time 
        time.sleep(7)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




