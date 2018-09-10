
# coding: utf-8

# In[1]:


from flask import Blueprint, render_template
from database_setup import TravelSensor, Summary
from database_init import db_session


# In[2]:


index = Blueprint('index', __name__)

@index.route("/", methods=['GET'])
def index_function():
    return render_template("index.html")

