
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, length

app = Flask(__name__)


SECRET_KEY = "efgh"
app.config['SECRET_KEY'] = SECRET_KEY


class MyForm(FlaskForm):
    """Contact/Location form."""
    location_1 = StringField(
        'Location_1',
        [DataRequired()]
    )
    
    location_2 = TextField(
        'Location_2',
        [
            DataRequired()
        ]
    )

    method = TextField(
        'Transportation Method',
        [
            DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')
    



@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    "this function is reading the html page to allow the user to fill out the form for a designated location"
    form = MyForm() 
    transportation = ["Train", "Bus", "Plane", "Car" ]
    
    return render_template('signin.html', form=form, transportation=transportation) 

from distance import lat_long, travel, saved, distance_calc
@app.route('/data', methods = ['POST'])
def data():
    """ Based on the location given in the form, the data will go to PArt1 and get the closest stop and if it is wheelchair accessible"""
    if request.method == "POST":
        location1 = request.form["location1"]
        location1= str(location1)
        location2 = request.form["location2"]
        location2 = str(location2)
        result = lat_long(location1, location2)
        if result == "none":
            return render_template("signin.html")
        else:
            result = result.split(",")
            return render_template("data_presentation.html", location1 = location1, location2 = location2)

# def diff_distance():
#     """run program from distance.lat_long--will print the distance between two points"""
#     location1 = Location_1
#     location2 = location_2
#     return lat_long(location1,location2), render_template('data_presentation.html', form = form)
# def saved_distance():
#     """ run program from sitance.distance_calc-- will calculate what was traveled and saved. 
#     Essentially combining the travel and saved functions from distance.py """
#     return distance_calc(), render_template('data_presentation.html', form=form)










if __name__ == "__main__":
    routes.run(debug=True)