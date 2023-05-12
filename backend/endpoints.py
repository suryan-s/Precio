import datetime
import json
import os
import secrets
import sqlite3

import pandas as pd
from dbutils.pooled_db import PooledDB

# import numpy as np
# import pandas as pd
# from keras.callbacks import EarlyStopping, ModelCheckpoint
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from keras.models import load_model

# from tensorflow.keras.layers import Dense
# from tensorflow.keras.models import Sequential

# {
#     "id":"string","
#     "name":"Agro",
#     "type":"Arable",
#     "available":"PMS",
#     "stationParameters":["Temperature","Humidity","Pressure","Wind","UV","Light","Rain","Battery Status"],
#     "pmsParameters":["Soil Moisture","Soil Temperature/Humidity"]
# }

# model = load_model(os.path.join('model','best_pretemp.h5'))

# Create a connection pool
pool = PooledDB(
    creator=sqlite3,
    database=os.path.join("database", "sql3.db"),
    maxconnections=100,  # Adjust the maximum number of connections as per your requirements
)

columns_WMS = {
            "date_time": "date_time TIMESTAMP",
            "maxtempC": "maxtempC INTEGER",
            "mintempC": "mintempC INTEGER",
            "uvIndex": "uvIndex INTEGER",
            "DewPointC": "DewPointC INTEGER",
            "FeelsLikeC": "FeelsLikeC INTEGER",
            "HeatIndexC": "HeatIndexC INTEGER",
            "WindChillC": "WindChillC INTEGER",
            "WindGustKmph": "WindGustKmph INTEGER",
            "humidity": "humidity INTEGER",
            "precipMM": "precipMM INTEGER",
            "pressure": "pressure INTEGER",
            "tempC": "tempC INTEGER",
            "visibility": "visibility INTEGER",
            "winddirDegree": "winddirDegree INTEGER",
            "windspeedKmph": "windspeedKmph INTEGER",
            "location": "location TEXT",
            "battery": "battery INTEGER",
            "status": "status TEXT",
            "update": "update TEXT"
        }


def get_client(input):
    incoming_json = json.dumps(input)
    incoming_json = json.loads(incoming_json)
    print(incoming_json)


def create_project(config):
    status = 500
    token = config["id"]
    print(token)
    pro_name = config["name"]
    pro_name = pro_name.replace(" ", "")
    table_name = str(pro_name) + "_" + str(token)
    table_name = table_name.replace(" ", "")
    print(table_name)
    create_table_sql = """"""
    if config["available"] == "Weather Station":
        # Define the SQL statement to create a new table
        create_table_sql = """CREATE TABLE {} (
                                date_time TIMESTAMP,
                                maxtempC INTEGER,
                                mintempC INTEGER,
                                uvIndex INTEGER,
                                DewPointC INTEGER,
                                FeelsLikeC INTEGER,
                                HeatIndexC INTEGER,
                                WindChillC INTEGER,
                                WindGustKmph INTEGER,
                                humidity INTEGER,
                                precipMM INTEGER,
                                pressure INTEGER,
                                tempC INTEGER,
                                visibility INTEGER,
                                winddirDegree INTEGER,
                                windspeedKmph INTEGER,
                                location TEXT
                            );""".format(
            table_name
        )
    elif config["available"] == "PMS":
        create_table_sql = """CREATE TABLE {} (
                                tempC INTEGER,
                                moisture INTEGER,
                                location TEXT
                            );""".format(
            table_name
        )

    conn = pool.connection()
    cursor = conn.cursor()
    try:
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

    # Check if the table was created successfully
    # print(c.execute("SELECT name FROM sqlite_master WHERE type='table';"))
    if f"{table_name}" in [
        table[0]
        for table in cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
    ]:
        print("Table created successfully.")
        settings = {}
        with open("settings.json", "r+") as f:
            settings = json.load(f)
            settings["table_names"].append(table_name)
            json.dump(settings, f)
        status = 200
        conn.commit()
    else:
        print("Error creating table.")
        status = 500

    if conn:
        cursor.close()
    return status


def delete_project(token):
    delete_sql = """DROP TABLE {};""".format(token)
    conn = pool.connection()
    status = 0
    data = None
    cursor = conn.cursor()
    try:
        val = cursor.execute(delete_sql)
        print("Deleted ", val)
        with open("settings.json", "r+") as content:
            data = json.load(content)
            data["table_names"].remove(token)
            json.dump(data, content)
        conn.commit()
        status = 200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    except Exception as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    if conn:
        cursor.close()
    return status


def insert_into_table_WMS(datapoints, token):
    insert_data_sql = """INSERT INTO {} (
        date_time, 
        maxtempC, 
        mintempC, 
        uvIndex, 
        DewPointC, 
        FeelsLikeC, 
        HeatIndexC, 
        WindChillC, 
        WindGustKmph, 
        humidity, 
        precipMM, 
        pressure, 
        tempC, 
        visibility, 
        winddirDegree, 
        windspeedKmph, 
        location
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""".format(
        token
    )
    conn = pool.connection()
    status = 0
    cursor = conn.cursor()
    try:
        cursor.execute(
            insert_data_sql,
            (
                datetime.datetime.now(),
                datapoints["maxtempC"],
                datapoints["mintempC"],
                datapoints["uvIndex"],
                datapoints["DewPointC"],
                datapoints["FeelsLikeC"],
                datapoints["HeatIndexC"],
                datapoints["WindChillC"],
                datapoints["WindGustKmph"],
                datapoints["humidity"],
                datapoints["precipMM"],
                datapoints["pressure"],
                datapoints["tempC"],
                datapoints["visibility"],
                datapoints["winddirDegree"],
                datapoints["windspeedKmph"],
                datapoints["location"],
            ),
        )
        conn.commit()
        if cursor.rowcount > 0:
            status = 200
        else:
            status = 204
    except sqlite3.OperationalError as e:
        print("Operational error: ", e)
        status = 404
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    except Exception as e:
        print(f"The insert_into_table_WMS failed with error: {e}")
        status = 500
    finally:
        if conn:
            cursor.close()
            # conn.close()
    return status


def get_gauge_data(token):
    get_data_sql = """SELECT date_time,  
        uvIndex,  
        HeatIndexC, 
        humidity, 
        precipMM, 
        pressure, 
        tempC,         
        windspeedKmph FROM {} ORDER BY date_time DESC LIMIT 1;""".format(
        token
    )
    conn = pool.connection()
    status = 0
    cursor = conn.cursor()
    data = {}
    result = None
    try:
        cursor.execute(get_data_sql)
        rows = cursor.fetchall()
        # print(rows[0])
        parameters = [
            "date_time",
            "uvIndex",
            "HeatIndexC",
            "humidity",
            "precipMM",
            "pressure",
            "tempC",
            "windspeedKmph",
        ]

        for row, parameter in zip(list(rows[0]), parameters):
            data[parameter] = row
            # print(row,parameter)

        conn.commit()
        status = 200
        result = json.dumps(data)
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            cursor.close()
    return result, status


def get_line_data(token, parameter):
    get_data_sql = """"""
    if parameter == 0:
        get_data_sql = """SELECT date_time, 
            maxtempC, 
            mintempC,
            tempC    
            FROM {} ORDER BY date_time DESC LIMIT 50;""".format(
            token
        )
    elif parameter == 1:
        get_data_sql = """SELECT date_time, 
            humidity FROM {} ORDER BY date_time DESC LIMIT 50;""".format(
            token
        )
    elif parameter == 2:
        get_data_sql = """SELECT date_time, 
            precipMM FROM {} ORDER BY date_time DESC LIMIT 50;""".format(
            token
        )
    elif parameter == 3:
        get_data_sql = """SELECT date_time, 
            pressure FROM {} ORDER BY date_time DESC LIMIT 50;""".format(
            token
        )

    conn = pool.connection()
    status = 0
    result = None
    cursor = conn.cursor()
    try:
        cursor.execute(get_data_sql)
        rows = cursor.fetchall()
        result = json.dumps(rows)
        conn.commit()
        status = 200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            cursor.close()
    return result, status


def get_table_names():
    table_names = """SELECT name FROM sqlite_master WHERE type='table';"""
    conn = pool.connection()
    status = 0
    result = None
    c = conn.cursor()
    try:
        c.execute(table_names)
        rows = c.fetchall()
        result = json.dumps(rows)
        conn.commit()
        status = 200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            c.close()
    return result, status


def insert_into_table_PMS(token, datapoints):
    tempC = datapoints["tempC"]
    moisture = datapoints["moisture"]
    location = datapoints["location"]
    pms_insert = (
        """INSERT into {} (tempC, moisture, location) VALUES (?, ?, ?);""".format(token)
    )
    conn = pool.connection()
    status = 0
    result = None
    cursor = conn.cursor()
    try:
        cursor.execute(pms_insert, (tempC, moisture, location))
        conn.commit()
        if cursor.rowcount > 0:
            result = "Execution successful"
            status = 200
        else:
            result = "No rows affected"
            status = 204
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    except Exception as e:
        print(f"The insert_into_table_PMS failed with error: {e}")
        status = 500
    if conn:
        cursor.close()
    return result, status


def load_sql_to_pandas(token: str):
    conn = sqlite3.connect(os.path.join("database", "sql3.db"))
    status = 0
    df = None
    query = """SELECT * FROM {};""".format(token)
    try:
        df = pd.read_sql_query(query, conn)
        print(df)
        status = 200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        return {"status": status, "data": "None" if df is None else df.to_json()}


def predictBasic():
    pass


def create_project_():
    config = {
        "name": "Home",
        "type": "Arable",
        "available": "Weather Station",
        "param": [
            "Temperature",
            "Humidity",
            "Pressure",
            "UV",
            "Light",
            "Visibility",
            "WindSpd",
            "WindDir",
            "Precipitation",
            "Battery",
            "Location",
            "Status",
            "Update",
        ],
    }
    status = 500
    token = secrets.token_hex(5)
    pro_name = config["name"].replace(" ", "")
    table_name = f"{pro_name}_{token}".replace(" ", "")
    print(f" Token: {token}, Table name: {table_name}")
    create_table_sql = "CREATE TABLE {} (date_time TIMESTAMP,location TEXT);".format(table_name)
    create_table_sql = ""
    
    if config["available"] == "Weather Station":
        
        for param in config["param"]:
            create_table_sql += columns_WMS[param] + ","
        create_table_sql = create_table_sql[:-1] + ");"
        print(create_table_sql)


create_project_()
