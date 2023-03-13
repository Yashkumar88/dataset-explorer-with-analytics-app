#---------- library --------------------
import array
import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import datetime

#---------
def main():
    st.title('YASH KAUSHIK DATASET EXPLORATORY DATA ANALYSIS')
    st.header('simple Data explore APP')
    
    def folder(folder_path='./mydatasets'):
        file_path= os.listdir(folder_path)
        select_name=st.selectbox('select your datasets',file_path)
        return os.path.join(folder_path,select_name)
    filename=folder()
    st.info(f'you selected {filename}')
    
   
    # show datasets
    df =pd.read_csv(filename)
    if st.checkbox('show full dataset'):
        st.write(df)
    if st.checkbox('columns'):
        number =st.number_input('enter the number of rows and columns:',5,10)
        st.dataframe(df.head(number))
        if st.checkbox("shape of Datasets"):
            st.write(df.shape)
            dmin=st.radio('check how many rows and columns in it',('rows','columns'))
            if dmin =='columns':
                st.write(df.shape[1])
            if dmin =='rows':
                st.write(df.shape[0])
    if st.checkbox('select columns to show'):
        all_columns =df.columns
        multi =st.multiselect('select',all_columns)
        new_df =df[multi]
        st.dataframe(new_df)
        if st.button('datatypes'):
            st.write(new_df.dtypes)
        if st.button('values_counts'):
            st.write(new_df.iloc[:,-1].value_counts())
        if st.button('summary of selected columns'):
            st.write(new_df.describe())
        
        
    # entire datasets----------------------------------------------------------    
    if st.button('summary of entire datasets'):
        st.write(df.describe())
   #
   
    
   # EDA PARTS ---------------------------------
   
    st.title('DATA Analytics Parts')
    #st.subheader('customerizable plots') 
    
    # Seaborn ----------------------------------------
    if st.checkbox('correlation Plot with seaborn'):
        #fig,ax =plt.subplot()
        if st.button('generate plots'):
            st.success('Generate a Pie Charts')
        
        
        sns.heatmap(df.corr(),annot=True)
        #A=st.write(sns.heatmap(df.corr(),annot=True))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
        
        
    #  countplots-------------------------------
    if st.checkbox(' plot the values'):
        st.text('values that can be targets')
        all_columns_name=df.columns.tolist()
        primary_col =st.selectbox("primary Columns to group by",all_columns_name)
        selected_columns_names = st.multiselect('select columns',all_columns_name)
        if st.button('plot'):
            st.text('Generate A plot')
            if selected_columns_names:
                vc_plot =df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot =df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
                
    
    # 
    # pie chart --------------------------
    
    if st.checkbox('Pie Plot'):
        all_columns_name =df.columns.tolist()
        if st.button('generate plots'):
            st.success('Generate a Pie Charts')
            #cust_data =df.iloc[:,-1].value_counts()
            fig, ax = plt.subplots()
            ax.pie(df.iloc[:,-1].value_counts(),autopct="%0.1f%%")
            #st.write(df.iloc[:,-1].value_counts().plot.pie(autopct ='%0.1f%%'))
            st.pyplot(fig)
    
    
    
    # area ,hist------------------------------------------------------------    
    all_columns_name =df.columns.tolist() # converts into lists
    type_of_plot =st.selectbox('select types of Plots',['area','bar','line','hist','box','kde'])
    selected_columns_names =st.multiselect('select Coloumns to plot',all_columns_name)
    
    if st.button('Generate Plots'):
        st.success('Generate Customerize plot of {} for {}'.format(type_of_plot,selected_columns_names))
    
    # plot the graphs on streamlits
        if type_of_plot == 'area':
            cust_data =df[selected_columns_names]
            st.area_chart(cust_data)
        elif type_of_plot =='line':
            cust_data =df[selected_columns_names]
            st.line_chart()
        elif type_of_plot =='bar':
            cust_data =df[selected_columns_names]
            st.bar_chart()
        elif type_of_plot =='hist':
            cust_data =df[selected_columns_names]
            #st.hist_chart()
            fig, ax = plt.subplots()
            ax.hist(cust_data, bins=20)
            st.pyplot(fig)
        elif type_of_plot =='box':
            cust_data =df[selected_columns_names]
            #st.hist_chart()
            fig, ax = plt.subplots()
            ax.boxplot(cust_data)
            st.pyplot(fig)
        
        # customerized
        
        # DATA PREPROCESSING'S---------------------------------------------
    if st.checkbox('checking null values'):
       st.write(df.isnull().sum())
    st.caption('if there is null values so apply two methods [triming,cappings]')
    if st.checkbox('removed datasets'):
        select_columns=st.multiselect('select multicolumns',all_columns_name)
        if st.button('remove null data'):
            a=st.write(df.drop(select_columns,axis=1))
   
          
            
        #    '''
    ##  downloads ----
    st.sidebar.download_button(label="Download data as CSV",data=df.to_csv(),file_name='large_df.csv',mime='text/csv')
   
if __name__ =='__main__':
    main()


    