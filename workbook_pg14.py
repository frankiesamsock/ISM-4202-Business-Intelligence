#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from sqlalchemy import create_engine

db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))
sql = "select * from scores"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[ ]:




