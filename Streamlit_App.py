import streamlit as st
import pickle as pk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Set page configuration for the webpage
st.set_page_config(page_title="Smartphone Price Predictor", page_icon="📱", layout="centered")
#import the datasets and the trained model
db0=pd.read_csv("python-project/GG.csv")
db1 = pd.read_csv('phone_data.csv')
db2 = pd.read_csv("dfAfterCleaning.csv")
pipe = pk.load(open("trained_model.pkl", "rb"))
#Set title to the webpage
st.title("Smartphone Price Predictor")
#Set tabs for the webpage
tab1, tab2 = st.tabs(["Prediction", "About Us"])
#Sort the brands alphabetically
brands = sorted(db1['Brand'].unique())
storage = sorted(db2['storage'].unique(), key=int)
ram = sorted(db2['Ram'].unique(), key=int)
inches = sorted(db2['Inches'].unique(), key=float)
battery = sorted(db2['Battery'].unique(), key=int)
cam = sorted(db2['Front Camera'].unique(), key=int)
OS = ['Android', 'iOS', 'Another OS']
#Deploy the tabs
with tab1:
    st.header("Price Prediction")
    st.caption("Select the specifications of the smartphone to predict the price and display the statistics")
    #Insert Selectboxs for the user to select the smartphone specefications divided into two columns
    col1, col2 = st.columns(2, gap="large")
    with col1:
        brandSelected = st.selectbox("Select brand", brands)
        storageSelected = st.selectbox("Select Storage (in gb)", storage)
        ramSelected = st.selectbox("Select Ram (in gb)", ram)
        incheSeleted = st.selectbox("Select Screen Size (in inches)", inches)

    with col2:    
        resolutionSelected = st.selectbox("Select Screen Resolution", ['1080x1620', '1080x1920', '1080x2400', '1080x2412', '1080x2460',
       '1170x2532', '1440x720', '1520x720', '1560x720', '1600x720',
       '160x120', '160x128', '1612x720', '1640x720', '1650x720',
       '1792x828', '2176x1812', '2208x1768', '2340x1080', '2376x1080',
       '2388x1080', '2400x1080', '2404x1080', '2408x1080', '2412x1080',
       '2436x1125', '2460x1080', '2532x1170', '2556x1179', '2640x1080',
       '2778x1284', '277x1284', '2796x1290', '3040x1440', '3088x1440',
       '3120x1440', '3200x1440', '320x240', '480x854', '720x1280',
       '720x1560', '720x1600', '720x1612', '720x1640', '720x1650',
       '828x1792', '900x1600', '960x480'])
        batterySelected = st.selectbox("Select Battery Capacity (in mah)", battery)
        camSelected = st.selectbox("Select Front Camera (in mp)", cam)
        OSSelected = st.selectbox("Select Operating System", OS)

    #Insert buttons for the user to predict the price and display the statistics
    col1, col2, col3, col4  = st.columns([1,1,1,1], gap="small")
    with col1:
        pass
    with col2:
        predictButton = st.button("Predict Price", type="primary")
    with col3:
        statsButton = st.button("Display Statistics", type="secondary")
    with col4:
        pass
    #configure variables and np arrays to be used in the prediction query
    widthSelected = int(resolutionSelected.split('x')[1])
    heightSelected = int(resolutionSelected.split('x')[0])
    osIndex = OS.index(OSSelected)
    OSSelected = np.zeros((len(OS),), dtype=int)
    OSSelected[osIndex] = 1
    brandIndex = brands.index(brandSelected)
    brandSelected = np.zeros((len(brands),), dtype=int)
    brandSelected[brandIndex] = 1
    #Function to search for the recommended smartphones
    def search_phone(storageSelected, ramSelected, camSelected, batterySelected):
        result = db1.loc[(db1['storage'] == str(storageSelected)) & (db1['Ram'] == str(ramSelected)) & (db1['Front Camera'] == str(camSelected)) & (db1['Battery'] == str(batterySelected))]
        phones = result.loc[:, ['title', 'storage', 'Ram', 'Front Camera', 'Battery']]
        phones.drop_duplicates(inplace=True)
        return phones
    #Function to add links to the recommended smartphones
    def add_links(title):
        title = title.replace(' ', '+')
        link = f'https://www.amazon.eg/s?k={title}'
        return link
    
    #insert statsButton & predictButton functionality
    if statsButton:
    	st.subheader("Statistics:")
    	cat = []
    	con = []

    	for i in db2.columns:
        	if db2[i].nunique() <= 9 and db2[i].nunique() > 2 or i=='category_column':
               		cat.append(i)
       		else:
               		con.append(i)

    	option = st.selectbox('How would you like to be presented?', ('Line Chart', 'Area Chart', 'chart3'))
    	if option == "Line Chart":
    		for i in cat:
    			st.line_chart(db2[f"{i}"], y=i)
    	elif option == "Area Chart":
    		for i in cat:
    			st.area_chart(db2[f"{i}"], y=i)
    	else:
        	st.error(option)

	
    if predictButton:
        #make a query array and pass it to the model to predict the price
        query = np.array([storageSelected, ramSelected, camSelected, batterySelected, incheSeleted, widthSelected, heightSelected])
        query = np.insert(query, 5, brandSelected)
        query = np.insert(query, -2, OSSelected)
        query = query.reshape(1, -1)
        predictedPrice = pipe.predict(query)
        #Display the predicted price range
        if(predictedPrice[0] == 1):
            st.subheader("The predicted price range is: 440 - 4463 EGP")
        elif(predictedPrice[0] == 2):
            st.subheader("The predicted price range is: 4463 - 7199 EGP")
        elif(predictedPrice[0] == 3):
            st.subheader("The predicted price range is: 7199 - 17399 EGP")
        elif(predictedPrice[0] == 4):
            st.subheader("The predicted price range is: 17399 - 80000 EGP")
        #insert divider and subheader
        st.divider()
        st.subheader("Recommended Smartphones")
        #Call the search_phone function to get the recommended smartphones
        phones = search_phone(storageSelected, ramSelected, camSelected, batterySelected)
        #Insert links to the recommended smartphones
        phones['Link'] = phones['title'].apply(add_links)
        #Display the recommended smartphones DataFrame in HTML table
        phones = phones.to_html(index=False, justify='center', render_links=True)
        st.write(phones, unsafe_allow_html=True)   
with tab2:
    #Insert information about the project
    st.subheader("About Our Smartphone Price Prediction Project")
    st.write("Welcome to our Smartphone Price Prediction project! We are a team of passionate programmers and university students with a shared interest in machine learning and technology.")
    st.subheader("Our Mission")
    st.write("Our mission is to simplify the process of buying a smartphone by providing users with a reliable price prediction tool. We understand that choosing the right smartphone can be a daunting task, given the plethora of options available in the market. That's why we've leveraged the power of machine learning to create a user-friendly solution that predicts smartphone prices based on their specifications.")
    st.subheader("How It Works?")
    st.write("Our project uses advanced machine learning algorithms to analyze and predict smartphone prices. Users can input the specifications of the smartphone they are interested in, and our system processes this data to generate accurate price estimates. Additionally, we provide detailed statistics and insights about the predicted price, helping users make informed decisions.")
    st.subheader("Why Choose Us?")
    st.markdown('''• **Accuracy**: Our machine learning models have been trained on extensive datasets, ensuring high accuracy in price predictions.''')
    st.markdown('''• **User-Friendly**: We have designed our platform to be intuitive and easy to use, making it accessible to both tech-savvy individuals and those new to the world of technology.''')
    st.markdown('''• **Constant Improvement**: We are committed to continuous improvement and regularly update our models to reflect the latest market trends and smartphone releases.''')
    st.subheader("Meet Our Team")
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    #Insert images and names of the team members
    with col1:
        st.image("photo.png", width=150)
        st.markdown("<h3 style='text-align: center; color: white;'>Ahmed Shaaban</h1>", unsafe_allow_html=True)
    with col2:
        st.image("photo.png", width=150)
        st.markdown("<h3 style='text-align: center; color: white;'>Khaled Farouq</h1>", unsafe_allow_html=True)
    with col3:
        st.image("photo.png", width=150)
        st.markdown("<h3 style='text-align: center; color: white;'>Emad Rabea</h1>", unsafe_allow_html=True)
    with col4:
        st.image("photo.png", width=150)
        st.markdown("<h3 style='text-align: center; color: white;'>Omar Hussien</h1>", unsafe_allow_html=True)
    with col5:
        st.image("photo.png", width=150)
        st.markdown("<h3 style='text-align: center; color: white;'>Mohamed Ahmed</h1>", unsafe_allow_html=True)
    #Insert divider
    st.divider()
    #Insert footer
    st.markdown(f'''<img src="https://github.com/fluidicon.png" alt="GitHub Icon" width="30" height="30"> Github Source Code: <a href={'https://github.com/Eng-Omar-Hussein/Predict_Mobile_Price'}>Github|Predict-Mobile-Price</a>''', unsafe_allow_html=True)
