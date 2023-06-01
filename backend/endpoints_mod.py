import json
import os
import secrets
import sqlite3
from datetime import datetime

import pandas as pd
from dbutils.pooled_db import PooledDB

# Create a connection pool
pool = PooledDB(
    creator=sqlite3,
    database=os.path.join("database", "sql3_mod.db"),
    maxconnections=100,  # Adjust the maximum number of connections as per your requirements
)

def create_table():
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            password_hash TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project_id TEXT PRIMARY KEY,
            project_name TEXT,
            project_created TIMESTAMP,
            project_description TEXT,
            project_type TEXT,
            user_id TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            device_id TEXT PRIMARY KEY,
            device_name TEXT,
            device_type TEXT,
            user_id INTEGER,
            project_id TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (userproject_id_id) REFERENCES projects(project_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            device_id TEXT,
            value TEXT,
            param TEXT,
            timestamp TIMESTAMP PRIMARY KEY,
            FOREIGN KEY (device_id) REFERENCES devices(device_id)
        )
    """ )
    conn.commit()
    cursor.close()    


def create_project(config):
    # config = {
    #     "name": "Project name",
    #     "description": "Project description",
    #     "type": "Project type"
    # }
    status = 500
    project_id = secrets.token_hex(8)
    project_name = config["name"]
    project_description = config["description"] if len(config["description"])!=0 else "None"
    project_type = config["type"] if len(config["type"])!=0 else "None"
    project_created = datetime.now()
    user_id = "user_id"
    print(f"Project created: {project_created}, Project name: {project_name}, Project ID: {project_id}, Project type: {project_type}, Project description: {project_description}")
    create_project_query = """
        INSERT INTO projects (project_id, project_name, project_created, project_description, project_type, user_id) VALUES (?, ?, ?, ?, ?, ?)
    """
    conn = pool.connection()
    cursor = conn.cursor()
    try:
        cursor.execute(create_project_query, (project_id, project_name, project_created, project_description, project_type, user_id))
        conn.commit()
        status = 200
    except sqlite3.Error as error:
        print(error)
        status = 500
    if conn: 
        cursor.close()
    return status