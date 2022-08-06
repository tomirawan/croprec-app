import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.write("""

# This app will give you the best crop recommendation to grow!

""")

from PIL import Image
img = Image.open('farm1.jpg')
st.image(img, width=750)

st.write(""" I'm using the ***Koppen Climate Classification*** to classify the climate condition. It was first published by German-Russian climatologist
Wladimir Köppen (1846–1940) in 1884, with several later modifications by Köppen, notably in 1918 and 1936.
The Köppen climate classification divides climates into five main climate groups,
with each group being divided based on average seasonal precipitation that used as parameter. Enjoy!
""")

st.sidebar.header('Parameter input')

#collects user input Parameter
#@st.cache
#def parameter_input():
with st.sidebar:

        climate = st.selectbox('Cilmate condition',('Tropical Wet','Tropical Wet and Dry',
        'Subtropical Dessert and Steppe','Mid-latitude Dessert and Steppe',
        'Mid-latitude Wet','Mid-latitude Winter-Dry','Mid-latitude Summer-Dry',
        'Polar Tundra','Polar Ice Cap'))

        if climate=='Tropical Wet':
            climate = 575
        elif climate=='Tropical Wet and Dry':
            climate = 289
        elif climate=='Subropical Dessert and Steppe':
            climate = 51
        elif climate=='Mid-latitude Dessert and Steppe':
            climate = 29
        elif climate=='Mid-latitude Wet':
            climate = 114
        elif climate=='Mid-latitude Winter-Dry':
            climate = 58
        elif climate=='Mid-latitude Summer-Dry':
            climate = 73
        elif climate=='Polar Tundra':
            climate = 9
        elif climate=='Polar Ice Cap':
            climate = 7
        else:
            pass

        st.markdown('Insert your soil condition parameters.')
        n = st.slider('Nitrogen : ', 5, 20, 100)
        p = st.slider('Phosporus : ', 5, 20, 100)
        k = st.slider('Potassium : ', 5, 20, 100)
        temp = st.slider('Temperature (C) : ', 5, 20, 45)
        hum = st.slider('Humidity : ', 5, 20, 100)
        ph = st.slider('pH : ', 1, 2, 10)

        data = {'n':n, 'p':p, 'k':k,
                'temperature':temp,
                'humidity':hum,
                'ph':ph,
                'rainfall':climate}
        feature = pd.DataFrame(data, index=[0])
        #return feature

#input_df = parameter_input()

raw_data = pd.read_csv('crop_recommendation.csv')
raw = raw_data.drop(columns=['label'])
df = pd.concat([feature,raw], axis=0)
df = df[:1]

load_clf = pickle.load(open('croprec_clf.pkl', 'rb'))
prediction = load_clf.predict(df)

st.write("""
This app will work with the specified parameters. You have to do your own test to get the parameters!
""")
st.subheader('Given parameter :')
col1, col2 = st.columns(2)
with col1:
    st.write("Nitrogen : ", n)
    st.write("Phospor : ", p)
    st.write("Potassium : ", k)
with col2:
    st.write("Ambient Temperature (C) : ", temp)
    st.write("Humidity : ", hum)
    st.write("pH Rate : ", ph)

st.write(' #### Crop Recommendation : \n', prediction[0])

#st.subheader('System Accuracy')
#st.write(accuracy)
