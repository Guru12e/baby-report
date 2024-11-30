from flask import Flask
from flask_cors import CORS
from babyReport import babyReport
from multiprocessing import Process
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
from waitress import serve
from apscheduler.schedulers.background import BackgroundScheduler

client = MongoClient(os.getenv("DATABASE_URL"))
database = client["AstroKids"]
collection = database["childDetails"]

def AstrokidsBot():
    six_hours_ago = datetime.now() - timedelta(hours=6)
    while True:
        print("Bot is running")
        try:
            pipeline = [
                {"$unwind": "$childDetails"}, 
                {"$match": {
                    "childDetails.addedAt": {"$lt": six_hours_ago}, 
                    "childDetails.isChecked": False  
                }},
                {"$project": {"childDetails": 1, "_id": 0}} 
            ]
            
            childDeatils = list(collection.aggregate(pipeline))
            print(childDeatils)
            for child in childDeatils:
                details = child["childDetails"]
                try:
                    generate_report(f"{details['dob']} {details['time']}",details['place'],details['gender'],details['name'])
                    print(f"{details['name']} report generated")
                    collection.update_one(
                        {"childDetails.orderId": details['orderId']},  
                        {"$set": {"childDetails.$.isChecked": True}} 
                    )
                    print(f"{details['name']} isChecked updated to True")
                    
                except Exception as e:
                    print(e)
                    time.sleep(60)
                    
        except Exception as e:
            print(e)
        
        time.sleep(300)

app = Flask(__name__)
CORS(app)

def generate_report(dob,location,gender,name):
    babyReport(dob,location,app.root_path,gender,name)
    print("Report generated")
    
    
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        AstrokidsBot,
        'interval',
        seconds=10,
        max_instances=999999  
    )
    scheduler.start() 
    print("Scheduler started")
    serve(app, host='0.0.0.0', port=5000)