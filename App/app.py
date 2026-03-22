import pandas as pd
import joblib
import streamlit as st



st.set_page_config(page_title='fraud_detection',page_icon='🛃',layout='centered')

st.title(':rainbow[Fraud Detection App]')


try:
    model = joblib.load("fraud_model.pkl")
except Exception as e:
    st.error('model')
    st.write(e)
    st.stop()

tab0,tab1,tab2,tab3,tab4 = st.tabs([
    'PHOTO',
    'ABOUT PROJECT',
    'USER INPUT',
    'VISUALIZATION',
    'ABOUT DEVELOPER'

])
with tab0:
    st.image(r'C:\Users\indur\OneDrive\Desktop\neural\fraud_detection\Gemini_Generated_Image_i45sm2i45sm2i45s.png',caption='FRAUD DETECTION')



with tab1: 
   
    st.subheader(':rainbow[About Project]')

    st.write('Developed a Fraud Detection System using machine learning to identify suspicious ' \
    'financial transactions. The project includes data preprocessing, feature engineering, and model training ' \
    'using Logistic Regression, Random Forest, and Gradient Boosting within Scikit-learn pipelines.' \
    ' Model performance was evaluated using accuracy, recall, precision, ROC-AUC, and confusion matrix with threshold tuning to handle class imbalance.' \
    ' The trained models were deployed through a Streamlit web application, allowing users to input transaction details and receive real-time fraud predictions.')

    st.write('''
    -**Technologies Used**
    -Python 
    -Scikit-learn 
    -Pandas / NumPy
   -Streamlit 
    -Machine Learning Pipelines
    -baseline model(**logistic regression**)
    -**Random Forest**
    -**GradientBoosting**
    -evaluation(**confusion matrix score,recall,fl_score,accuracy**)
    -joblib('saving ')
    -matplotlib
    -Seaborn
    -mysql
    power bi
     ''')
with tab2:
    with st.form('click there to check fraud'):

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('user_input')
            amount = st.number_input('Amount', max_value=1000000, min_value=1)
            customer_age = st.number_input('Age', max_value=100, min_value=1)
            device = st.selectbox('Device', ['Desktop','Phone','Mobile','Tablet'])

        with col2:
            location = st.selectbox('Location', ['Germany','UK','Russia','Canada','India','USA'])
            payment_method = st.selectbox('Payment Method',['Debit Card','Crypto','Credit Card'])
            merchant = st.selectbox('Merchant',['Target','Amazon','Flipkart','Starbucks','Aliexpress','Cryptoex','Applestore','Ebay'])
            merchant_category = st.selectbox('Category',['Gadgets','Digital','Finance','Electronics','Retail','Food'])

        submit = st.form_submit_button('predict')


if submit:
    input_df = pd.DataFrame([{
        'amount':amount,
        'customer_age':customer_age,
        'device':device,
        'location':location,
        'payment_method':payment_method,
        'merchant':merchant,
        'merchant_category':merchant_category                          

    }])


    try:
        features = model.feature_names_in_

        features_data = pd.DataFrame(columns=features)
        features_data.loc[0] = '0'

        for col in input_df.columns:
            if col in features_data.columns:
                features_data[col] = input_df[col]
        
        feature_type = features_data.astype(str)

        y_pred = model.predict(feature_type)[0]
        y_prob = model.predict_proba(feature_type)[0][1]
        st.write(f'probability:{y_prob:.2f}')
        process_values = int(y_prob*100)
        st.progress(process_values)


        if y_pred == 1:
            st.error('Fraud Detected')
            st.snow()
            st.image(r'C:\Users\indur\OneDrive\Desktop\neural\fraud_detection\OIP.jpg',caption='FRAUD')
        else:
            st.success('Safe Transaction')
            st.balloons()
            st.image(r'C:\Users\indur\OneDrive\Desktop\neural\fraud_detection\OIP (1).jpg',caption='SAFE')

    except Exception as e:
        st.success('prediction fails')
        st.write(e)



with tab3:
    df = pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\neural\fraud_detection\feature_engineering.csv')
    col1,col2 = st.columns(2)
    with st.form('visualization'):

        with col1:
            st.subheader('**amount per location (sum)**')
            data = df.groupby('location')['amount'].sum()
            st.bar_chart(data)

        with col2:
            st.subheader('**fraud vs non fraud**')
            fraud_count = df['fraud'].value_counts() 
            st.bar_chart(fraud_count)


with tab4:
    st.subheader('**ABOUT DEVELOPER**')

    st.markdown(
        ''' I am a B.Tech student in Computer Science at Chalapathi Institute of Engineering and Technology
        with a strong interest in Data Science and Machine Learning. 

        I have experience working with Python, MySQL, Power BI, and data analysis tools, and 
        I enjoy building end-to-end data projects. My focus is on data-driven problem solving,
          including machine learning model development, 
        data preprocessing, and building interactive dashboards.

        -[GitHub](https://github.com/avinashreddy0)
        -[linkedin](https://www.linkedin.com/in/avinash-reddy-induri-4662b832a/')

        **skill**
        -python
        -pandas
        -numpy
        -matplotlib
        -seaborn
        -scikit-learn
        -machine learning
        -power bi
        -mysql
        -ETL
        -statistic
        -streamlit(deploy)
        -ANN and DNN
        
        ''')
    
    st.subheader('connect with me')
    st.write('NAME:INDURI AVINASH REDDY')

    st.write('phone-No:9346739650')
    st.write('Email:induriavinashreddy05@gmail.com')
                

