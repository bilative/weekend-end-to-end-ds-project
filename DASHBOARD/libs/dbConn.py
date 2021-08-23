import pymongo
import pandas as pd

ip = 'ip of the mongodb docker container'
client = pymongo.MongoClient(host=f'{ip}', port=27017)

db = client["weekend_project"]
collection = db["cars"]


def insert_all_to_mongodb():
    # This function will run only 1 time manually to imigrate csv data to mongodb
    # I'll do this after I deploy the app, by entering the container of this app
    # By run initiate_db.py file
    try:
        df = pd.read_csv('../DATA/scraped_data.csv')
        df['counts'] = 1
        df['Bodytype'] = df['Bodytype'].fillna('Suv')
        #This one explained in analyzing step. (4 is mode value so "Suv")
        df = df.fillna(0)
        # This one is also explained, Nano means not exist, so we fill them with 0
        data = df.to_dict('records')
        collection.insert_many(data)
        print('Succesfull!')
    except Exception as ex:
        print(ex)
        print('There is a problem!!')

def read_all():
    return pd.DataFrame(collection.find({}, {'_id': 0}))