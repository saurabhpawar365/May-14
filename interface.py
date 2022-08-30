from flask import Flask,jsonify,render_template,request
import numpy as np
import config
from project_app.utils import MedicalInsurance

app = Flask(__name__)
@app.route('/predicted_charges')
def get_insurance_charges():
    data = request.form
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    smoker = data['smoker']
    children = eval(data['children'])
    region = data['region']

    print('age,sex,bmi,smoker,children,region',age,sex,bmi,smoker,children,region)

    med_ins = MedicalInsurance(age,sex,bmi,smoker,children,region)
    charges = med_ins.get_predicted_charges()
    return jsonify({'result' : f'predicted value is : {charges}'})


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)

