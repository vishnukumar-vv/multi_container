from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://db:27017/")
db = client.mydb

@app.route("/")
def home():
    return "CI CD Python Multi Container App"

@app.route("/count")
def count():
    c = db.visits
    c.insert_one({"v":1})
    return f"Visits: {c.count_documents({})}"

app.run(host="0.0.0.0", port=5000)
