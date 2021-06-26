#################################################
# Dependencies Setup
#################################################

import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import all_
from sqlalchemy import log
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, render_template, jsonify, request, redirect

#################################################
# Database Setup
#################################################
engine = create_engine("postgresql://postgres:postgres@localhost:5432/alcohol_analysis")
# inspector=inspect(engine)
# test = inspector.get_table_names()
# print(test)

# # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# # Save reference to the table
Beer = Base.classes.beer
Happiness = Base.classes.happiness
PerCapita = Base.classes.per_capita_alcohol_1890

# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)


# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/beer")
def beer():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return beer data"""
    results = session.query(Beer.country_name,Beer.year,Beer.beer_consumption).all()

    session.close()

    return jsonify(results)

@app.route("/api/happiness")
def happiness():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return happiness data"""
    results = session.query(Happiness.country_name, Happiness.year, Happiness.life_ladder).all()

    session.close()

    return jsonify(results)

@app.route("/api/per_capita_alcohol_1890")
def per_capita():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return happiness data"""
    results = session.query(PerCapita.entity, PerCapita.code, PerCapita.year, PerCapita.alcohol_consumption).all()

    session.close()

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
