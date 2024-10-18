#!/usr/bin/env python
# coding: utf-8

# In[2]:



import streamlit as st



# In[3]:


import streamlit as st
# 设置全局属性
st.set_page_config(
    page_title='页面标题',
    page_icon='☆☆☆ ',
    layout='wide'
)

# 正文
#st.image('./all_data/pic/star.webp')
st.title('首页')
st.markdown('> Streamlit 支持通过 st.markdown 直接渲染 markdown')
st.divider()
"# 1级标题"
"## 2级标题"
"### 3级标题"
"#### 4级标题"
"##### 5级标题"
"###### 6级标题"
st.divider()
st.write('*欢迎使用我的主页* :sunglasses:')

# In[ ]:




