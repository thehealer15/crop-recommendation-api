from flask import Flask
from flask import Flask,request,jsonify
import numpy as np
import pickle
app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
        return "hello world"

@app.route('/recommend',methods=['POST'])
def predict():
        """Parameters be nitrogen, phosphorus, potassium, temperature, humidity, PH, rainfall"""
        nitrogen = request.form.get('nitrogen')
        phosphorus = request.form.get('phosphorus')
        potassium = request.form.get('potassium')
        temperature = request.form.get('temperature')
        humidity = request.form.get('humidity')
        PH = request.form.get('PH')
        rainfall = request.form.get('rainfall')
        
        input_query = np.array([[nitrogen,phosphorus,potassium,temperature,humidity,PH,rainfall]])
        input_query = input_query.reshape(1,-1)
        predict1 = model.predict(input_query)
        crop_name = str()
        crop_dict = dict()
        crop_list = ['Apple(सेब)','Banana(केला)','Blackgram(काला चना)','Chickpea(काबुली चना)','Coconut(नारियल)',
                'Coffee(कॉफ़ी)','Cotton(कपास)','Grapes(अंगूर)','Jute(जूट)','Kidneybeans(राज़में)','Lentil(मसूर की दाल)',
                'Maize(मक्का)','Mango(आम)','Mothbeans(मोठबीन)','Mungbeans(मूंग)','Muskmelon(खरबूजा)', 'Orange(संतरा)', 'Papaya(पपीता)', 'Pigeonpeas(कबूतर के मटर)', 'Pomegranate(अनार)', 'Rice(चावल)', 'Watermelon(तरबूज)']
        
        
#         crop_dict = {0:'Apple(सेब)',1:'Banana(केला)',2: 'Blackgram(काला चना)',3:'Chickpea(काबुली चना)',4:'Coconut(नारियल)'
#                 5:'Coffee(कॉफ़ी)',6:'Cotton(कपास)',7:'Grapes(अंगूर)',8:'Jute(जूट)',9:'Kidneybeans(राज़में)',10:'Lentil(मसूर की दाल)'
#                 11:'Maize(मक्का)',12:'Mango(आम)',13:'Mothbeans(मोठबीन)',14:'Mungbeans(मूंग)',15:'Muskmelon(खरबूजा)', 16:'Orange(संतरा)'
# , 17:'Papaya(पपीता)', 18:'Pigeonpeas(कबूतर के मटर)',19: 'Pomegranate(अनार)',20: 'Rice(चावल)',21: 'Watermelon(तरबूज)'}
        
        # return jsonify({'crop':crop_list[int(predict1)] })

        return jsonify({'crop':crop_list[predict1[0].item()] })

if __name__ == '__main__':
    app.run(debug=True)