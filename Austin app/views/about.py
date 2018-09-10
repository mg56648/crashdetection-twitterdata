
# coding: utf-8

# In[1]:


from flask import Blueprint, render_template


# In[2]:


aboutUs = Blueprint('aboutUs', __name__)


# In[3]:


@aboutUs.route("/aboutUs", methods=['GET'])
def aboutUs_function():
    return render_template("aboutUs.html")

