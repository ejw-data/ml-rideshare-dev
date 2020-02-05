# Dependencies
# ----------------------------------  https://github.com/pallets/flask-sqlalchemy/issues/98
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric
from flask_marshmallow import Marshmallow 
import simplejson

app = Flask(__name__)

# ENV = 'prod'

# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/election_db'
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bdwrgfxtgonvby:333ccd10d6c1f8d04a9c2bd3023b9e48b343371559c97a034a28080decf9892c@ec2-107-22-216-123.compute-1.amazonaws.com:5432/d6cd55jo1ktp4t'

# app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class Election(db.Model): 
#     __tablename__ = 'districts'
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String)  
#     last_name = db.Column(db.String)  
#     first_elected = db.Column(db.Integer) 
#     birth_year = db.Column(db.Integer)   
#     votepercent_president2016_democrat = db.Column(db.Float) 
#     votepercent_president2016_republican = db.Column(db.Float) 
   
 


#     def __init__(self, first_name, last_name, first_elected, birth_year, votepercent_president2016_democrat, votepercent_president2016_republican):
#         self.first_name = first_name
#         self.last_name = last_name 
#         self.first_elected = first_elected 
#         self.birth_year = birth_year 
#         self.votepercent_president2016_democrat = votepercent_president2016_democrat 
#         self.votepercent_president2016_republican = votepercent_president2016_republican 
        

# class ElectionSchema(ma.ModelSchema):
#     class Meta:
#         model = Election
#         json_module = simplejson



@app.route('/')    # removed:  , methods=['GET']
def index():
    # test = db.session.query(Election).all()
    # for record in test:
    #     print(record.x)

    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit_fare():

    if request.method == 'POST':
        start_location = request.form['startLoc']
        end_location = request.form['endLoc']
        print(start_location, end_location)

        if start_location == '' or end_location == '':
            return render_template('index.html', message='Please complete all sections of the form')
        elif start_location != '' and end_location != '':
            return render_template('index.html', estimator='5.25')
        else:
            return render_template('index.html', estimator='')

        # Mapquest and mapbox:  https://www.mapquestapi.com/directions/v2/route?key=6aMCYSpGBo4Eg20Lw7RljQ0nXcUGsA5S&from=Denver%2C+CO&to=Boulder%2C+CO&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false
    return render_template('index.html', estimator='')
        

if __name__ == '__main__':
    app.debug = True
    app.run()




