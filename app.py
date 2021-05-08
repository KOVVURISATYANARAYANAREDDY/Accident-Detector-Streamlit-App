import streamlit as st 
from PIL import Image
import classify 
import numpy as np
import time


lab = {
	0:'Accidents',
	1:'dense_traffic',
	2:'Fire',
	3:'sparse_traffic'
        }

st.title("Accident Detector🚗🚕🚙🚎🚌🚐🚒🚖🚘🚍🚔🚑🚓")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:

        image = Image.open(uploaded_file)
       
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.write("Result...")
                image.save('current.jpg')
                label,bool = classify.predict(image.resize((224,224)))
                label = label[0]
                res = lab[np.argmax(label)]
                l = round(label[np.argmax(label)]*100,2)
                st.markdown(res +" : "+ str(l) + "%")
                if bool:
                      st.markdown(" An Email has been sent to a nearby Hospital. ")
                      now = time.localtime()
                      t = time.strftime("%H:%M:%S", now)
                      st.write(t)
                      #st.write(type(t))