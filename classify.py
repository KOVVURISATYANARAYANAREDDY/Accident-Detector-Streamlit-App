from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import streamlit as st
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('team5.h5')
        print('Model Loaded')
        return model 

label = {
	0:"Accident",
	1:"Dense_traffic",
	2:"Fire",
	3:"Sparse_traffic"
}

        
def predict(image):
        loaded_model = get_model()
        #image = load_img(image, target_size=(224, 224))
        image = img_to_array(image)
        image = image/255.0
        image = np.reshape(image,[1,224,224,3])

        classes = loaded_model.predict(image)
        if np.argmax(classes[0]) == 0 or np.argmax(classes[0]) == 2:
                res = trigger(label[np.argmax(classes[0])])
                return classes, res

        return classes, False

reciever = <<ENTER OTHER MAIL ID>>
#str(dt_string)

def trigger(predict):
       msg = MIMEMultipart()
       message = predict + " was Detected."
       password = <<ENTER YOUR PASSWORD>>
       msg['From'] = <<ENTER YOUR MAIL ID>>
       msg['To'] = "manikantasanjay1999@gmail.com"
       msg['Subject'] = "Accident Detector."
       msg.attach(MIMEText(message, 'plain'))
       with open('current.jpg', 'rb') as fp:
               img = MIMEImage(fp.read())
               img.add_header('Content-Disposition', 'attachment', filename="current.jpg")
               msg.attach(img)
       #msg.attach(MIMEImage(open("current.jpg").read()))
       # create server
       
       server = smtplib.SMTP('smtp.gmail.com: 587')
       server.starttls()
       # Login Credentials for sending the mail
       server.login(msg['From'], password)
       # send the message via the server.
       server.sendmail(msg['From'], msg['To'], msg.as_string())
       server.quit()
       return True

