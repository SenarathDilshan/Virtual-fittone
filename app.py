from flask import Flask, render_template, request
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import classification_report


import pickle


app = Flask(__name__)

#def prediction(lst):
    #filename = './model/predictor.pickle'
    #with open(filename, 'rb') as file:
        #model = pickle.load(file)
    #pred_value = model.predict([lst])
    #return pred_value 


@app.route('/', methods=['POST','GET'])
def index():
  if request.method == 'POST':
    Chest = request.form ['Chest']
    Shoulder = request.form['Shoulder']
    Length = request.form['Length']
    Brand = request.form['brandname']
    Type = request.form['Type']
    
    
    
    #print(Chest,Shoulder,Length,Brand,Type)

    feature_list =[]
    feature_list.append(float(Chest))
    feature_list.append(float(Shoulder))
    feature_list.append(float(Length))
    
    Brand_list = ['Brand Name_Robato']
    Type_list = ['Type_slim fit','Type_trim fit']

    for item in Brand_list:
      if item == Brand:
        feature_list.append(1)
      else:
        feature_list.append(0)

    for item in Type_list:
      if item == Type:
        feature_list.append(1)
      else:
        feature_list.append(0)    

    print(feature_list)
     
    #pred = prediction(feature_list)
    #print(pred)
   
  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)
