from flask import Flask,render_template,request
from weather import main as get_weather_info

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    data=None
    if request.method == 'POST':
        city=request.form['cityname']
        state = request.form['statename']
        country = request.form['countryname']
        data=get_weather_info(city,state,country)
    return render_template('index.html',data=data)




if __name__=='__main__':
    app.run(debug=True)












