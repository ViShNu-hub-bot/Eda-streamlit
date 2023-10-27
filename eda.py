import numpy as np 
import pandas as pd
import streamlit as st
from ydata_profiling import profilereport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''
            **Exploratorey Data Analysis App**
            
            This app created using the **pandas-Profiling Library** ''')

with st.sidebar.header('1. Upload your csv data'):
    uploaded_file = st.sidebar.file_uploader("upload your csv file",type=["csv"])
    st.sidebar.markdown("""
                        [Example csv input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)""")
    
    if uploaded_file is not None:
        @st.cache_data
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
        df = load_csv()
        pr = profilereport(df,explorative=True)
        st.header('**Input Dataframe**')
        st.write(df)
        st.header('**pandas profiling report**')
        st_profile_report(pr)
    else:
        st.info('Awaiting for csv file to be uploaded.')
        if st.button('press to use sample dataset'):
            @st.cache_data
            def load_data():
                a=pd.DataFrame(
                    np.random.rand(100,5),
                    columns=['a','b','c','d','e']
                )
                return a
            df = load_data()
            pr=profilereport(df,explorative=True)
            st.write(df)
            st.write('----')
            st.header('**Pandas Profiling report')
            st_profile_report(pr)
            
                    
            
            

        
    

