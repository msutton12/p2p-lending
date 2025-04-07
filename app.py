from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Listing
import os


app = Flask(__name__)

# ---------- DATABASES ----------

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'p2p.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listings')
def listings():
    all_listings = Listing.query.all()
    return render_template('listings.html', listings=all_listings)


@app.route('/listing/<int:listing_id>')
def listing_detail(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return render_template('listing_detail.html', listing=listing)

@app.route('/add-listing', methods=['GET', 'POST'])
def add_listing():
    if request.method == 'POST':
        title = request.form['title']
        founder = request.form['founder']
        description = request.form['description']
        goal = float(request.form['goal'])
        image1 = request.form['image1']
        image2 = request.form['image2']
        video = request.form['video']

        new_listing = Listing(
            title=title,
            founder=founder,
            description=description,
            goal=goal,
            image1=image1,
            image2=image2,
            video=video
        )
        db.session.add(new_listing)
        db.session.commit()
        flash('Listing created successfully!')
        return redirect(url_for('listings'))

    return render_template('add_listing.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/mentors')
def mentors():
    sample_mentors = ['Tina F.', 'James D.', 'Elena V.']
    return render_template('mentors.html', mentors=sample_mentors)

@app.cli.command('create-db')
def create_db():
    db.create_all()
    print("📦 Database created successfully!")


# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
