# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    founder = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal = db.Column(db.Float, nullable=False)
    raised = db.Column(db.Float, default=0.0)
    image1 = db.Column(db.String(200))
    image2 = db.Column(db.String(200))
    video = db.Column(db.String(200))
