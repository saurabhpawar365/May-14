import json
import pickle
import config
import nump as np



class MedicalInsurance():
    def __init__ (self,age,sex,bmi,smoker,children,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.smoker = smoker
        self.children = children
        self.region =  'reg_' + region


    def load_model(self):
        with open (config.MODEL_FILE_PATH, 'rb') as f :
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH, 'r') as f :
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_model()
        print('*'*30,self.json_data)
        region_index = self.json_data['columns'].index(self.region)
        array1 = np.zeros(len(self.json_data['columns']),dtype = int)
        array1[0] = self.age
        array1[1] = self.json_data['sex'][self.sex]
        array1[2] = self.bmi
        array1[3] = self.children 
        array1[4] = self.json_data['smoker'][self.smoker]
        array1[5] = region_index = 1
        print('array1 :',array1)
        predicted_charges = np.around(self.model.predict([array1])[0],2)
        return predicted_charges

if __name__ == '__main__':
    age= 19.0
    sex= 'female'
    bmi= 77.9
    children= 0.0
    smoker= 'no'
    region = 'northeast'
    med_ins = MedicalInsurance(age,sex,bmi,smoker,children,region)
    med_ins.get_predicted_charges()
        
    



