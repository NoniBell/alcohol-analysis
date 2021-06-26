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
CleanedSales = Base.classes.cleaned_sales
Happiness = Base.classes.happiness
PerCapita = Base.classes.per_capita_alcohol_1890
Spirits = Base.classes.spirits
Wine = Base.classes.wine


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

    beer_list = []

    for country_name, year, beer_consumption in results:
        beer_dict={}
        beer_dict["country_name"] = country_name
        beer_dict["year"] = year
        beer_dict["beer_consumption"] = beer_consumption
        beer_list.append(beer_dict)

    return jsonify(beer_list)

@app.route("/api/cleaned_sales")
def cleaned_sales():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return sales data"""
    results = session.query(CleanedSales.year, CleanedSales.fips, CleanedSales.beverage, CleanedSales.gallons, CleanedSales.ethanol).all()

    session.close()
    
    sales_list = []

    for year, fips, beverage, gallons, ethanol in results:
        sales_dict={}
        sales_dict["year"] = year
        sales_dict["year"] = fips
        sales_dict["beverage"] = beverage
        sales_dict["gallons"] = gallons
        sales_dict["ethanol"] = ethanol
        sales_list.append(sales_dict)

    return jsonify(sales_list)

@app.route("/api/happiness")
def happiness():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return happiness data"""
    results = session.query(Happiness.country_name, Happiness.year, Happiness.life_ladder).all()

    session.close()

    happiness_list = []

    for country_name, year, life_ladder in results:
        happiness_dict={}
        happiness_dict["country_name"] = country_name
        happiness_dict["year"] = year
        happiness_dict["life_ladder"] = life_ladder
        happiness_list.append(happiness_dict)

    return jsonify(happiness_list)

@app.route("/api/per_capita_alcohol_1890")
def per_capita():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return per capita data"""
    results = session.query(PerCapita.entity, PerCapita.code, PerCapita.year, PerCapita.alcohol_consumption).all()

    session.close()

    per_capita_list = []

    for entity, code, year, alcohol_consumption in results:
        per_capita_dict={}
        per_capita_dict["entity"] = entity
        per_capita_dict["code"] = code
        per_capita_dict["year"] = year
        per_capita_dict["alcohol_consumption"] = alcohol_consumption
        per_capita_list.append(per_capita_dict)

    return jsonify(per_capita_list)


@app.route("/api/spirits")
def spirits():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return spirits data"""
    results = session.query(Spirits.country_name,Spirits.year,Spirits.spirits_consumption).all()

    session.close()

    spirits_list = []

    for country_name, year, spirits_consumption in results:
        spirits_dict={}
        spirits_dict["country_name"] = country_name
        spirits_dict["year"] = year
        spirits_dict["beer_consumption"] = spirits_consumption
        spirits_list.append(spirits_dict)

    return jsonify(spirits_list)


@app.route("/api/wine")
def wine():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return wine data"""
    results = session.query(Wine.country_name,Wine.year,Wine.wine_consumption).all()

    session.close()

    wine_list = []

    for country_name, year, wine_consumption in results:
        wine_dict={}
        wine_dict["country_name"] = country_name
        wine_dict["year"] = year
        wine_dict["beer_consumption"] = wine_consumption
        wine_list.append(wine_dict)

    return jsonify(wine_list)


if __name__ == '__main__':
    app.run(debug=True)
