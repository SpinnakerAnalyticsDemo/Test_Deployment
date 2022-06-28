from flask import Flask, request, render_template
import pickle

app=Flask(__name__,template_folder='template')
model = pickle.load(open('modelout.pkl', 'rb'))  # loading the model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    Xval = int(request.form["Xval"])
    prediction = model.predict([[Xval]])
    output = round(prediction[0], 2) 

    return render_template('index.html', prediction_text=f'Based on your input of {Xval}, Your Predicted Value is ${output}')
  
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)