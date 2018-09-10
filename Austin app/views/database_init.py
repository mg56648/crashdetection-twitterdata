
# coding: utf-8

# In[1]:


# Configuration
# import os
# import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# In[2]:


from database_setup import Base


# In[3]:


engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(bind=engine))

