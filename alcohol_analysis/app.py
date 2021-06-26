#################################################
# Dependencies Setup
#################################################
import numpy as np
import sqlalchemy
from sqlalchemy import log
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import all_

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("postgres://inxfrugjxzmzvt:30397674e5eb04cab5642ff927df03b23770e5ef461659ec4dd366e4f63d6d7e@ec2-35-171-250-21.compute-1.amazonaws.com:5432/d279tqqg4p4i79")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://inxfrugjxzmzvt:30397674e5eb04cab5642ff927df03b23770e5ef461659ec4dd366e4f63d6d7e@ec2-35-171-250-21.compute-1.amazonaws.com:5432/d279tqqg4p4i79', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create Classes and initialize
class AlcoholC(db.Model):
    __tablename__ = 'alcohol_consumption_per_person_us'
    id = db.Column(db.Integer, primary_key=True)
    Entity = db.Column(db.String)
    Code = db.Column(db.String)
    Year = db.Column(db.Integer)
    Spirits = db.Column(db.Float)
    Beer = db.Column(db.Float)
    Wine = db.Column(db.Float)

    def __init__(self, Entity, Code, Year, Spirits, Beer, Wine):
        self.Entity = Entity
        self.Code = Code
        self.Year = Year
        self.Spirits = Spirits
        self.Beer = Beer
        self.Wine = Wine

class AlcoholS(db.Model):
    __tablename__ = 'alcsales2017to2020'
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer)
    Month = db.Column(db.Integer)
    FIPS = db.Column(db.Integer)
    Beverage = db.Column(db.Integer)
    Gallons = db.Column(db.Float)
    Ethanol = db.Column(db.Float)
    Population = db.Column(db.Float)
    PerCapita = db.Column(db.Float)
    PerCapita3yr = db.Column(db.Float)
    PctChange = db.Column(db.Float)

    def __init__(self, Year, Month, FIPS,Beverage, Gallons,Ethanol,Population,PerCapita,PerCapita3yr,PctChange):
        self.Year = Year
        self.Month = Month
        self.FIPS = FIPS
        self.Beverage = Beverage
        self.Gallons = Gallons
        self.Ethanol = Ethanol
        self.Population = Population
        self.PerCapita = PerCapita
        self.PerCapita3yr = PerCapita3yr
        self.PctChange = PctChange

class Beer(db.Model):
    __tablename__ = 'beer'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String)
    code = db.Column(db.String)
    year = db.Column(db.Integer)
    beer_consumption = db.Column(db.Float)

    def __init__ (self,country_name, code, year, beer_consumption):
        self.country_name = country_name
        self.code = code
        self.year = year
        self.beer_consumption = beer_consumption

class BeerC(db.Model):
    __tablename__ = 'beer_consumption_per_person'
    id = db.Column(db.Integer, primary_key=True)
    Entity = db.Column(db.String)
    Code = db.Column(db.String)
    Year = db.Column(db.Integer)
    Beer = db.Column(db.Float)

    def __init__(self, Entity, Code, Year, Beer):
        self.Entity = Entity
        self.Code = Code
        self.Year = Year
        self.Beer = Beer
        
class CleanedSales(db.Model):
    __tablename__ = 'cleaned_sales'
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer)
    Month = db.Column(db.Integer)
    FIPS = db.Column(db.Integer)
    Beverage = db.Column(db.Integer)
    Gallons = db.Column(db.Float)
    Ethanol = db.Column(db.Float)
    Population = db.Column(db.Float)
    PerCapita = db.Column(db.Float)
    PerCapita3yr = db.Column(db.Float)
    PctChange = db.Column(db.Float)

    def __init__(self, Year, Month, FIPS,Beverage, Gallons,Ethanol,Population,PerCapita,PerCapita3yr,PctChange):
        self.Year = Year
        self.Month = Month
        self.FIPS = FIPS
        self.Beverage = Beverage
        self.Gallons = Gallons
        self.Ethanol = Ethanol
        self.Population = Population
        self.PerCapita = PerCapita
        self.PerCapita3yr = PerCapita3yr
        self.PctChange = PctChange

class Happiness(db.Model):
    __tablename__ = 'happiness'
    id = db.Column(db.Integer, primary_key=True)
    country_name= db.Column(db.String)
    year = db.Column(db.Integer) 
    life_ladder = db.Column(db.Float)
    log_gdp_per_capita = db.Column(db.Float)
    social_support = db.Column(db.Float)
    healthy_life_expectancy_at_birth = db.Column(db.Float)
    freedom_to_make_life_choices = db.Column(db.Float)
    generosity = db.Column(db.Float)
    perceptions_of_corruption = db.Column(db.Float)
    positive_effect = db.Column(db.Float)
    negative_effect = db.Column(db.Float)

    def __init__(self,country_name,year,life_ladder,log_gdp_per_capita,social_support, healthy_life_expectancy_at_birth,freedom_to_make_life_choices,generosity,perceptions_of_corruption,positive_effect,negative_effect):
        self.country_name = country_name
        self.year = year
        self.life_ladder = life_ladder
        self.log_gdp_per_capita = log_gdp_per_capita
        self.social_support = social_support
        self.healthy_life_expectancy_at_birth = healthy_life_expectancy_at_birth
        self.freedom_to_make_life_choices = freedom_to_make_life_choices
        self.generosity = generosity
        self.perceptions_of_corruption = perceptions_of_corruption
        self.positive_effect = positive_effect
        self.negative_effect = negative_effect

class PCAlcohol(db.Model):
    __tablename__ = 'per_capita_alcohol_1890'
    id = db.Column(db.Integer, primary_key=True)
    Entity = db.Column(db.String)
    Code = db.Column(db.String)
    Year = db.Column(db.Integer)
    alcohol_consumption = db.Column(db.Float)

    def __init__(self, Entity, Code, Year, alcohol_consumption):
        self.Entity = Entity
        self.Code = Code
        self.Year = Year
        self.alcohol_consumption = alcohol_consumption

class Spirits(db.Model):
    __tablename__ = 'spirits'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String)
    code = db.Column(db.String)
    year = db.Column(db.Integer)
    spirits_consumption = db.Column(db.Float)

    def __init__ (self,country_name, code, year, spirits_consumption):
        self.country_name = country_name
        self.code = code
        self.year = year
        self.spirits_consumption = spirits_consumption

class SpiritsC(db.Model):
    __tablename__ = 'spirits_consumption_per_person'
    id = db.Column(db.Integer, primary_key=True)
    Entity = db.Column(db.String)
    Code = db.Column(db.String)
    Year = db.Column(db.Integer)
    Spirits = db.Column(db.Float)

    def __init__(self, Entity, Code, Year, Spirits):
        self.Entity = Entity
        self.Code = Code
        self.Year = Year
        self.Spirits = Spirits

class Wine(db.Model):
    __tablename__ = 'wine'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String)
    code = db.Column(db.String)
    year = db.Column(db.Integer)
    wine_consumption = db.Column(db.Float)

    def __init__ (self,country_name, code, year, wine_consumption):
        self.country_name = country_name
        self.code = code
        self.year = year
        self.wine_consumption = wine_consumption

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/alcohol_consumption_per_person_us")   
def  alcohol_consumption_per_person_us():
    session = Session(engine)
    results = session.query(AlcoholC.all).all()
    session.close()
    all_alcohol= []
    for entity, code, year, spirits, beer, wine in results:
        all_dict = {}
        all_dict["Entity"] = entity
        all_dict["Code"] = code
        all_dict["Year"] = year
        all_dict["Spirits"] = spirits
        all_dict["Beer"] = beer
        all_dict["Wine"] = wine
        all_alcohol.append(all_dict)
    return jsonify(all_alcohol)

@app.route("/api/alcsales2017to2020")
def alcsales2017to2020():
    session = Session(engine)
    results = session.query(AlcoholS.all).all()
    session.close()
    all_sales= []
    for year, month, FIPS, beverage, gallons, ethanol, population, per_capita, per_capita_3yr, pct_change in results:
        sales_dict = {}
        sales_dict["Year"] = year
        sales_dict["Month"] = month
        sales_dict["FIPS"] = FIPS
        sales_dict["Beverage"] = beverage
        sales_dict["Gallons"] = gallons
        sales_dict["Ethanol"] = ethanol
        sales_dict["Population"] = population
        sales_dict["PerCapita"] = per_capita
        sales_dict["PerCapita3yr"] = per_capita_3yr
        sales_dict["PctChange"] = pct_change
        all_sales.append(sales_dict)
    return jsonify(all_sales)

@app.route("/api/beer")
def beer():
    session = Session(engine)
    results = session.query(Beer.all).all()
    session.close()
    all_beer = []
    for country_name, year, beer_consumption in results:
        beer_dict = {}
        beer_dict["country_name"] = country_name
        beer_dict["year"] = year
        beer_dict["beer_consumption"] = beer_consumption
        all_beer.append(beer_dict)
    return jsonify(all_beer)

@app.route("/api/beer_consumption_per_person")
def beer_consumption_per_person():
    session = Session(engine)
    results = session.query(BeerC.all).all()
    session.close()
    all_beerc= []
    for entity, code, year, beer in results:
        beerc_dict = {}
        beerc_dict["Entity"] = entity
        beerc_dict["Code"] = code
        beerc_dict["Year"] = year
        beerc_dict["Beer"] = beer
        all_beerc.append(beerc_dict)
    return jsonify(all_beerc)

@app.route("/api/cleaned_sales")
def cleaned_sales():
    session = Session(engine)
    results = session.query(CleanedSales.all).all()
    session.close()
    clean_sales= []
    for year, month, FIPS, beverage, gallons, ethanol, population, per_capita, per_capita_3yr, pct_change in results:
        clean_dict = {}
        clean_dict["Year"] = year
        clean_dict["Month"] = month
        clean_dict["FIPS"] = FIPS
        clean_dict["Beverage"] = beverage
        clean_dict["Gallons"] = gallons
        clean_dict["Ethanol"] = ethanol
        clean_dict["Population"] = population
        clean_dict["PerCapita"] = per_capita
        clean_dict["PerCapita3yr"] = per_capita_3yr
        clean_dict["PctChange"] = pct_change
        clean_sales.append(clean_dict)
    return jsonify(clean_sales)

@app.route("/api/happiness")
def happiness():
    session = Session(engine)
    results = session.query(Happiness.all).all()
    session.close()
    happiness_list= []
    for country_name, year, life_ladder in results:
        happiness_dict = {}
        happiness_dict["country_name"] = country_name
        happiness_dict["year"] = year
        happiness_dict["life_ladder"] = life_ladder
        happiness_list.append(happiness_dict)
    return jsonify(happiness_list)

@app.route("/api/per_capita_alcohol_1890")
def per_capita_alcohol_1890():
    session = Session(engine)
    results = session.query(PCAlcohol.all).all()
    session.close()
    all_sales= []
    for year, month, FIPS, beverage, gallons, ethanol, population, per_capita, per_capita_3yr, pct_change in results:
        sales_dict = {}
        sales_dict["Year"] = year
        sales_dict["Month"] = month
        sales_dict["FIPS"] = FIPS
        sales_dict["Beverage"] = beverage
        sales_dict["Gallons"] = gallons
        sales_dict["Ethanol"] = ethanol
        sales_dict["Population"] = population
        sales_dict["PerCapita"] = per_capita
        sales_dict["PerCapita3yr"] = per_capita_3yr
        sales_dict["PctChange"] = pct_change
        all_sales.append(sales_dict)
    return jsonify(all_sales)

@app.route("/api/spirits")
def spirits():
    session = Session(engine)
    results = session.query(Spirits.all).all()
    session.close()
    all_spirits = []
    for country_name, year, spirits_consumption in results:
        spirits_dict = {}
        spirits_dict["country_name"] = country_name
        spirits_dict["year"] = year
        spirits_dict["spirits_consumption"] = spirits_consumption
        all_spirits.append(spirits_dict)
    return jsonify(all_spirits)

@app.route("/api/spirits_consumption_per_person")
def spirits_consumption_per_person():
    session = Session(engine)
    results = session.query(SpiritsC.all).all()
    session.close()
    all_spiritsc= []
    for entity, code, year, spirits in results:
        spiritsc_dict = {}
        spiritsc_dict["Entity"] = entity
        spiritsc_dict["Code"] = code
        spiritsc_dict["Year"] = year
        spiritsc_dict["Spirits"] = spirits
        all_spiritsc.append(spiritsc_dict)
    return jsonify(all_spiritsc)

@app.route("/api/wine")
def wine():
    session = Session(engine)
    results = session.query(Wine.all).all()
    session.close()
    all_wine = []
    for country_name,year, wine_consumption in results:
        wine_dict = {}
        wine_dict["country_name"] = country_name
        wine_dict["year"] = year
        wine_dict["wine_consumption"] = wine_consumption
        all_wine.append(wine_dict)
    return jsonify(all_wine)


if __name__ == '__main__':
    app.run(debug=True)