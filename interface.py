from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import MedicalInsurence
import config
import traceback
app = Flask(__name__)

@app.route('/medical_insurence')
def home():
    return render_template('medical_insurence.html')

@app.route('/predict_charges', methods = ['GET', 'POST'])
def predict_charges():
    try:
        if request.method == 'GET':
            print("+"*50)
            data = request.args.get
            print("Data :",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = int(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            Obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
            
            # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
            return render_template('medical_insurence.html', prediction = pred_price)

        elif request.method == 'POST':
            print("*"*40)
            data = request.form.get
            print("Data :",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = int(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            Obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
            
            # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
            return render_template('medical_insurence.html', prediction = pred_price)

    except:
        print(traceback.print_exc())
        return redirect(url_for('medical_insurence'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
