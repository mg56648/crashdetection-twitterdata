
# coding: utf-8

# In[1]:


from flask import Blueprint, render_template


# In[2]:


problemStatement = Blueprint('problemStatement', __name__)


# In[3]:


problemStatement.route("/problemStatement")
def problemStatement_function():
    return render_template("problemStatement.html")

