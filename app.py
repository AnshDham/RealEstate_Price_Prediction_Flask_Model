from flask import Flask, request, render_template
import joblib
import webbrowser

app = Flask(__name__)
model = joblib.load('price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    distance = float(request.form['distance'])
    stores = int(request.form['stores'])

    prediction = model.predict([[age, distance, stores]])
    price = round(prediction[0], 2)
    return render_template('index.html', prediction=price)

if __name__ == '__main__':
    print("✅ Flask app launching")
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=False)








