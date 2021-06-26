from .app import db

class AlcoholC(db.Model):
    __tablename__ = 'alcohol_consumption_per_person_us'

    Entity = db.Column(db.String(250))
    Code = db.Column(db.String(250))
    Year = db.Column(db.Integer)
    Spirits = db.Column(db.Float)
    Beer = db.Column(db.Float)
    Wine = db.Column(db.Float)

class AlcoholS(db.Model):
    __tablename__ = 'alcsales2017to2020'

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

class Beer(db.Model):
    __tablename__ = 'beer'

    country_name = db.Column(db.String(250))
    code = db.Column(db.String(250))
    year = db.Column(db.Integer)
    beer_consumption = db.Column(db.Float)

class BeerC(db.Model):
    __tablename__ = 'beer_consumption_per_person'

    Entity = db.Column(db.String(250))
    Code = db.Column(db.String(250))
    Year = db.Column(db.Integer)
    Beer = db.Column(db.Float)

class CleanedSales(db.Model):
    __tablename__ = 'cleaned_sales'

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

class Happiness(db.Model):
    __tablename__ = 'happiness'

    country_name= db.Column(db.String(250))
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

class PCAlcohol(db.Model):
    __tablename__ = 'per_capita_alcohol_1890'

    Entity = db.Column(db.String(250))
    Code = db.Column(db.String(250))
    Year = db.Column(db.Integer)
    alcohol_consumption = db.Column(db.Float) 

class Spirits(db.Model):
    __tablename__ = 'spirits'

    country_name = db.Column(db.String(250))
    code = db.Column(db.String(250))
    year = db.Column(db.Integer)
    spirits_consumption = db.Column(db.Float)

class SpiritsC(db.Model):
    __tablename__ = 'spirits_consumption_per_person'

    Entity = db.Column(db.String(250))
    Code = db.Column(db.String(250))
    Year = db.Column(db.Integer)
    Spirits = db.Column(db.Float)

class Wine(db.Model):
    __tablename__ = 'wine'

    country_name = db.Column(db.String(250))
    code = db.Column(db.String(250))
    year = db.Column(db.Integer)
    wine_consumption = db.Column(db.Float)
