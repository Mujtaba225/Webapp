# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 02:11:54 2022

@author: SRC
"""

import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt





def main():
    st.title('Dropdown')
    data = pd.read_csv('SMS_data.csv',encoding='unicode_escape')
    label = st.selectbox("Label",list(data['Label'].unique()))
    st.table(data[data['Label']==label])
    #st.table(data)
    
    
    
    
    
    
    
    
if __name__=='__main__':
    main()
   
