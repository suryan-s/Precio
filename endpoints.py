import datetime
import json
import os
import sqlite3

# {     
#     "id":"string"," 
#     "name":"Agro",
#     "type":"Arable",
#     "available":"PMS",
#     "stationParameters":["Temperature","Humidity","Pressure","Wind","UV","Light","Rain","Battery Status"],
#     "pmsParameters":["Soil Moisture","Soil Temperature/Humidity"]
# }

def get_client(input):
    incoming_json = json.dumps(input)
    incoming_json  = json.loads(incoming_json)
    print(incoming_json)
    
def create_project(config):
    status =500
    token = config['id']
    print(token)
    pro_name = config['name']
    pro_name = pro_name.replace(' ','')
    table_name = str(pro_name) + '_' + str(token)
    table_name = table_name.replace(' ','')
    print(table_name)
    create_table_sql = ''''''
    if config['available'] == 'Weather Station':
    # Define the SQL statement to create a new table
        create_table_sql = '''CREATE TABLE {} (
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
                            );'''.format(table_name)
    elif config['available'] == 'PMS':
        create_table_sql = '''CREATE TABLE {} (
                                tempC INTEGER,
                                moisture INTEGER,
                                location TEXT
                            );'''.format(table_name)
    # print(create_table_sql)
    # db_files = glob.glob(os.path.join('database', '*.db'))
    db_name = os.path.join('database','sql3.db')
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:           
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
    
    # Check if the table was created successfully
    # print(c.execute("SELECT name FROM sqlite_master WHERE type='table';"))
    if '{}'.format(table_name) in [table[0] for table in c.execute("SELECT name FROM sqlite_master WHERE type='table';")]:
        print("Table created successfully.")
        settings = {}
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            print(settings)
        new_table_list = []
        new_table_list = settings['table_names']
        new_table_list.append(table_name)
        settings['table_names'] = new_table_list
        with open('settings.json', 'w') as f:
            f.write(json.dumps(settings))
        status = 200
    else:
        print("Error creating table.")
    conn.commit()
    conn.close()
    return status
    
def delete_project(token):
    delete_sql = '''DROP TABLE {};'''.format(token)
    conn = sqlite3.connect(os.path.join('database','sql3.db'))
    status = 0
    c = conn.cursor() 
    try:          
        c.execute(delete_sql)
        conn.commit()
        status =200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            conn.close()
            return status
        
# create_project("24k3423","weather")
#garden_ZBFZCz9Ugn

def insert_into_table(datapoints,token):
    db_name = ""
    tb_name = "" 
    with open('settings.json', 'r') as f:
        data = json.load(f)
        # db_name = data['database']
    tb_name = token
    date_time = datetime.datetime.now()
    maxtempC = datapoints['maxtempC']
    mintempC = datapoints['mintempC']
    uvIndex =   datapoints['uvIndex']
    DewPointC =    datapoints['DewPointC']
    FeelsLikeC =   datapoints['FeelsLikeC']
    HeatIndexC =  datapoints['HeatIndexC']
    WindChillC = datapoints['WindChillC']
    WindGustKmph = datapoints['WindGustKmph']
    humidity = datapoints['humidity']
    precipMM = datapoints['precipMM']
    pressure = datapoints['pressure']
    tempC = datapoints['tempC']
    visibility = datapoints['visibility']
    winddirDegree = datapoints['winddirDegree']
    windspeedKmphL = datapoints['windspeedKmph']
    location = datapoints['location']
    
    insert_data_sql = '''INSERT INTO {} (
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
        ) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(tb_name, date_time, maxtempC, mintempC, uvIndex, DewPointC, FeelsLikeC, HeatIndexC, WindChillC, WindGustKmph, humidity, precipMM, pressure, tempC, visibility, winddirDegree, windspeedKmphL, location)
    conn = sqlite3.connect(os.path.join('database','sql3.db'))
    status = 0
    c = conn.cursor() 
    try:          
        c.execute(insert_data_sql)
        conn.commit()
        status =200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            conn.close()
            return status
        
def get_gauge_data(token):
    get_data_sql = '''SELECT date_time, 
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
        winddirDegree, 
        windspeedKmph FROM {} ORDER BY date_time DESC LIMIT 1;'''.format(token)
    conn = sqlite3.connect(os.path.join('database','sql3.db'))
    status = 0
    c = conn.cursor() 
    data = {}
    result = None
    try:          
        c.execute(get_data_sql)
        rows = c.fetchall()
        parameters = [
            'date_time','maxtempC','mintempC','uvIndex',
            'DewPointC','FeelsLikeC','HeatIndexC','WindChillC',
            'WindGustKmph','humidity','precipMM','pressure',
            'tempC','winddirDegree','windspeedKmph'
        ] 
            
        for row,parameter in zip(rows,parameters):
            data[str(row)] = parameter
            
        conn.commit()
        status =200
        result = json.dumps(data)
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            conn.close()
            return result,status
        
def get_line_data(token):
    get_data_sql = '''SELECT date_time, 
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
        winddirDegree,
        windspeedKmph FROM {} ORDER BY date_time DESC LIMIT 20;'''.format(token)
    conn = sqlite3.connect(os.path.join('database','sql3.db'))
    status = 0
    result = None
    c = conn.cursor() 
    try:          
        c.execute(get_data_sql)
        rows = c.fetchall()  
        result = json.dumps(rows)          
        conn.commit()
        status =200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            conn.close()
            return result,status
        
def get_table_names():
    table_names = '''SELECT name FROM sqlite_master WHERE type='table';'''
    conn = sqlite3.connect(os.path.join('database','sql3.db'))
    status = 0
    result = None
    c = conn.cursor() 
    try:          
        c.execute(table_names)
        rows = c.fetchall()  
        result = json.dumps(rows)          
        conn.commit()
        status =200
    except sqlite3.Error as e:
        print(f"The SQL statement failed with error: {e}")
        status = 500
    finally:
        if conn:
            conn.close()
            return result,status
        
        
# print(get_line_data('Garden_B5gWZiq83M'))
# print(get_table_names())
# print(delete_project('Farmland_OBVL0EJnB0'))
# print(get_gauge_data('Garden_B5gWZiq83M'))