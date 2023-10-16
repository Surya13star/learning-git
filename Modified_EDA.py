import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import seaborn as sns
import missingno

def create_missing_values_bar(df):
    missing_fig = plt.figure(figsize = (10,5))
    ax = missing_fig.add_subplot(111)
    missingno.bar(df, figsize = (10,5), fontsize = 12, ax = ax)
    return missing_fig

col1, col2 = st.columns(2)

with col1:
   st.markdown("## Analayse Your Data Quickly with Easy_study") 
with col2:
    st.image("analyzing.jpg")

uploaded_file = st.file_uploader("Choose a CSV file to analyze")


if uploaded_file is not None:
    def load_data():
        data = pd.read_csv(uploaded_file)
        return pd.DataFrame(data)
    a = load_data()
    rows = len(a.index)
    columns = len(a.columns)
    a1 = a[a.duplicated()]
    duplicates = len(a1.index)
    st.write('Rows :{}'.format(rows))
    st.write('columns :{}'.format(columns))
    st.write('Duplicates :{}'.format(duplicates))
    #st.subheadert('Feautures :{}'.format(
    

    
    #st.write('Rows: {}'.format(categorical_columns))
    tab1, tab2, tab3 = st.tabs(["Data set Overview", "Individual Columns Stat", "Build your charts"])
    with tab1:
        st.subheader('1. Dataset')
        st.write(a)
        
        numeric_cols = a.select_dtypes(include=['int', 'float']).columns.tolist()
        numeric_columns = len(numeric_cols)
        categorical_cols = a.select_dtypes(include =['object']).columns.tolist()
        categorical_columns = len(categorical_cols)
        
        with cols1:
            st.subheader('Numeric columns')
            st.write('numerical columns: {}'.format(numeric_columns))
            st.write(numeric_cols)
        with cols2:
            st.subheader('Categorical or String columns')
            st.write('categorical columns: {}'.format(categorical_columns))
            st.write(categorical_cols)
        st.subheader('2. Dataset Overview')
        st.markdown("<span style ='font-weight:bold;'>{}</span> {} ".format("Rows :",rows), unsafe_allow_html=True)
        st.markdown("<span style ='font-weight:bold;'>{}</span> {} ".format("Duplicate rows:", duplicates), unsafe_allow_html = True)
        st.markdown("<span style = 'font-weight:bold;'>{}</span> {} ".format("Features :", columns), unsafe_allow_html = True)

        if st.checkbox('statisttics'):
            st.table(a.describe())

        if st.checkbox('Correlation'):
            fig,ax = plt.subplots(figsize = (8,3))
            sns.heatmap(a.corr(numeric_only = True),annot=True, cmap = "coolwarm")
            st.pyplot(fig)
        
    with tab2:
        if st.checkbox('Missing values Distribution'):
            missing_fig = create_missing_values_bar(a)
            st.pyplot(missing_fig, use_container_width = True)


        st.subheader('Understanding continuos feature')
        c=st.selectbox('Select Continuos feature', numeric_cols)
        st.write('Mean: {}'.format(a[c].mean()))
        st.write('Count: {}'.format(a[c].count()))
        st.write('Standard deviation: {}'.format(a[c].std()))
        st.write('Maximum: {}'.format(a[c].max()))
        st.write('Minimum: {}'.format(a[c].min()))
        st.markdown("<span style='font-weight:bold;'>{}</span>:".format("Quantiles"),unsafe_allow_html = True)
        st.write(a[[c]].quantile(0.25),a[[c]].quantile(0.5),a[[c]].quantile(0.75))    #entertin the dataframe and the feature with double square brackets gives         it in the form of a table
        #st.write(a[[c]].T[['25%',"50%","75%"]])

        b = st.checkbox('histogram')
        if (b == 'histogram'):
            fig, ax1 = plt.subplots(figsize = (8,3))
            sns.histplot(data = a, x= a[c])
            st.pyplot(fig)
            #st.bar_chart(data=a,x=a[c], y=None, color=None, width=8, height=8, use_container_width=True)
            #arr = a[c]
            #fig, ax = plt.subplots()
            #ax.hist(arr,bins=20)
            #st.pyplot(fig)
            #hist_data = a[c]
            #group_labels = ['group1']
            #fig = ff.create_distplot(hist_data,group_labels, bin_size = [0.5])
            #st.plotly_chart(fig,use_container_width = True)        
        
    with tab3:

        i=st.selectbox('Select x axis',categorical_cols)
        o=st.selectbox('Select y axis', numeric_cols)
        d=st.selectbox('Select the kind of chart and plot',('bar_chart','line plot','density plot','histogram','box plot'))
        if d =='bar_chart':
            fig,ax1 = plt.subplots(figsize = (8,3))
            sns.barplot(x=i,y=o,data = a)
            st.pyplot(fig)
        elif d =='histogram':
            fig, ax1 = plt.subplots(figsize = (8,3))
            sns.histplot(data = a, x= i, y = o)
            st.pyplot(fig)
        elif d=='density plot':
            fig, ax1 = plt.subplots(figsize = (8,3))
            sns.kdeplot(data = a, x = o)
            st.pyplot(fig)
        elif d=='box plot':
            fig, ax1 = plt.subplots(figsize = (8,3))
            sns.boxplot(data = a, x = i, y = o)
            st.pyplot(fig)
        elif d=='line plot':
            fig, ax1 = plt.subplots(figsize = (8,3))
            sns.lineplot(data = a, x = i, y = o)
            st.pyplot(fig)
        else:
            st.write('Select a option to plot the data')

    

        
            
   
        
    
    