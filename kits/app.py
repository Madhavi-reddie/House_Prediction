from flask import Flask,render_template,request
from args import *
import numpy as np 
import pickle
with open('Model.pkl','rb') as mod:
    model=pickle.load(mod)
with open('Scaler.pkl','rb') as mod:
    scaler=pickle.load(mod)
app=Flask(__name__)
@app.route('/',methods=['Get','POST'])
def index():
    #print(request.method)
    #print(request.form)
    if request.method== 'POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bathrooms']
        location=request.form['location']
        Area=request.form['Area']
        direction=request.form['direction']
        status=request.form['status']
        property_type=request.form['property_type']
        input_array=np.array([[bedrooms,bathrooms,location,
                              Area,direction,status,property_type]])
        t_array=scaler.transform(input_array)
        prediction=model.predict(t_array)[0]
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               property_type_mapping=property_type_mapping,prediction=prediction )   
    else:
        
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               property_type_mapping=property_type_mapping,
                               direction_mapping=direction_mapping)
        
@app.route('/second')
def second():
    return 'I am in Second Page'
@app.route('/third')
def third():
    return 'I am in Third Page' 
if __name__=='__main__':
    #app.run(use_reloader=True,debug=True)
    app.run()


