#first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for
#second line says we'll use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
#third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
import scraping

#to set up Flask:
app = Flask(__name__)

#to tell Python how to connect to Mongo using PyMongo:
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#let's define the route for the HTML page
@app.route("/")
#This function is what links our visual representation of our work, our web app, to the code that powers it.
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#function will set up our scraping route. Module 10.5.1
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

#The final bit of code we need for Flask is to tell it to run.
if __name__ == "__main__":
   app.run()


