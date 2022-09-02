# FLASK_APP CREATION SCRIPT:
# By Carly Sandler
# ----------------------------
# ---------------------------- 

# ----------------------------
# 1. SET UP THE FLASK WEATHER APP
# ----------------------------

# Import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependency
from flask import Flask, jsonify

# -----------------------------
# 2. SET UP THE DATABASE
# -----------------------------

# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create the classes variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# -----------------------------
# 3. SET UP FLASK
# -----------------------------

# Use magic method __name__ to check file source of running code
import app
print("example __name__ = %s", __name__)

if __name__ == "__main__":
	print("example is being run directly.")
else:
	print("example is being imported")

# Define the Flask app
app = Flask(__name__)

# -----------------------------
# 4. CREATE THE WELCOME ROUTE
# -----------------------------

# Define the welcome route
@app.route("/")

# Add the routing information for each of the other routes
def welcome():
	return(
	'''
	Welcome to the Climate Analysis API!
	Available Routes:
	/api/v1.0/precipitation
	/api/v1.0/stations
	/api/v1.0/tobs
	/api/v1.0/temp/start/end
	''')

# -----------------------------
# 5. PRECIPITATION ROUTE
# -----------------------------

# Create precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
def precipitation():
	# Calculate the date one year ago from the most recent date
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

	# Query: get date and precipitation for prev_year
	precipitation = session.query(Measurement.date,Measurement.prcp) .\
		filter(Measurement.date >= prev_year).all()
		
	# Create dictionary w/ jsonify()--format results into .JSON
	precip = {date: prcp for date, prcp in precipitation}
	return jsonify(precip)

# -----------------------------
# 6. STATIONS ROUTE
# -----------------------------

@app.route("/api/v1.0/stations")

def stations():
	results = session.query(Station.station).all()
	# Unravel results into one-dimensional array with:
		# `function np.ravel()`, `parameter = results`
	# Convert results array into a list with `list()`
	stations = list(np.ravel(results))
	return jsonify(stations=stations) 

# NOTE: `stations=stations` formats the list into JSON
# NOTE: Flask documentation: https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify

# -----------------------------
# 7. MONTHLY TEMPERATURE ROUTE
# -----------------------------

@app.route("/api/v1.0/tobs")

def temp_monthly():
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
	results = session.query(Measurement.tobs).\
		filter(Measurement.station == 'USC00519281').\
		filter(Measurement.date >= prev_year).all()
	temps = list(np.ravel(results))
	return jsonify(temps=temps)

# -----------------------------
# 8. STATISTICS ROUTE
# -----------------------------

# Provide both start and end date routes:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Add parameters to `stats()`: `start` and `end` parameters
def stats(start=None, end=None):
	# Query: min, avg, max temps; create list called `sel`
	sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

	# Add `if-not` statement to determine start/end date
	if not end:
		results = session.query(*sel).\
			filter(Measurement.date >= start).\
			filter(Measurement.date <= end).all()
		temps = list(np.ravel(results))
	return jsonify(temps=temps)

		# NOTE: (*sel) - asterik indicates multiple results from query: minimum, average, and maximum temperatures

	# Query: Calc statistics data
	results = session.query(*sel).\
		filter(Measurement.date >= start).\
		filter(Measurement.date <= end).all()
	temps = list(np.ravel(results))
	return jsonify(temps=temps)

	# NOTE: /api/v1.0/temp/start/end route -> [null,null,null]
	# NOTE: Add following to path to address in browser:
		# /api/v1.0/temp/2017-06-01/2017-06-30
		# result: ["temps":[71.0,77.21989528795811,83.0]]



