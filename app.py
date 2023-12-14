from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your machine learning model
with open("blood.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the values from the form
        R = int(request.form['R'])
        F = int(request.form['F'])
        M = int(request.form['M'])
        T = int(request.form['T'])
        
        # Prepare the data for prediction
        data = [[R, F, M, T]]
        
        # Make a prediction using the model
        prediction = model.predict(data)
        
        # Determine the prediction result
        if prediction == 1:
            return render_template('submit.html', prediction_result="Blood Centre 1")
        else:
            return render_template('submit.html', prediction_result="Blood Centre 2")
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
