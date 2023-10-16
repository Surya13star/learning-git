import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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
    

    cols1 ,cols2 = st.columns(2)
    numeric_cols = a.select_dtypes(include=['int', 'float']).columns.tolist()
    numeric_columns = len(numeric_cols)
    categorical_cols = a.select_dtypes(include =['object']).columns.tolist()
    categorical_columns = len(categorical_cols)
    st.write('Rows: {}'.format(categorical_columns))
    with cols1:
        st.subheader('Displays the numeric columns of the data set')
        st.write('numerical columns: {}'.format(numeric_columns))
        st.write(numeric_cols)
    with cols2:
        st.subheader('Displays the categorical or string columns of the data set')
        st.write('categorical columns: {}'.format(categorical_columns))
        st.write(categorical_cols)
    
    #st.header('Select the two columns to build charts and plots')
    #b = st.multiselect('select columns to build charts and plots',numeric_cols)
    
    #st.write('You selected:', b)

    st.subheader('Creating a chart for your easy understanding')

    x1 = st.text_input('enter the variable for x axis')
    x2 = st.text_input('enter the variable for y axis')

    x3 = st.selectbox('select the chart type', ('','bar chart', 'line chart'))

    if x3 == 'bar chart':
        st.bar_chart(data = a, x = str(x1), y = str(x2))
        st.write('you selected', x3)
    
    elif x3 == 'line chart':
        st.line_chart(data=a,x=str(x1), y=str(x2))
    elif x3 == '':
        st.write('select a type of chart or plot')
    

    #elif x3 == 'pie chart':
        
    
    # Creating a statistical summary viewing option by using a check box
    if st.checkbox('statisttics'):
        st.table(a.describe())

    # Creating a Correlation graph by using a heat map 
    if st.checkbox('Correlation'):
        fig,ax = plt.subplots(figsize = (8,3))
        sns.heatmap(a.corr(numeric_only = True),annot=True, cmap = "coolwarm")
        st.pyplot(fig)

    i=st.selectbox('Select x axis',categorical_cols)
    o=st.selectbox('Select y axis', numeric_cols)

    # Select a graph or chart to plot
    #st.checkbox('barchart')
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
   
                     
        
        
        
        




        



        
    
    




    






