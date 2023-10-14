# import csv

import mysql.connector

# TODO: REPLACE THE VALUE OF VARIABLE team (EX. TEAM 1 --> team = 1)
team = 0


# Requirement1: create schema ( name: DMA_team## )
def requirement1(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Creating schema...")

    # TODO: WRITE CODE HERE
    cursor.execute("CREATE DATABASE IF NOT EXISTS DMA_team07")
    # TODO: WRITE CODE HERE
    cursor.close()


# Requierement2: create table
def requirement2(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Creating tables...")

    # TODO: WRITE CODE HERE
    cursor.execute("USE DMA_team07")
    cursor.execute("DROP TABLE USER")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USER(
    Uid INT NOT NULL,
    Unickname VARCHAR(20), 
    PRIMARY KEY (Uid)) ;               
                   """)
    filepath = '/Users/yunseonghwan/Desktop/2023-2/데이터 관리와 분석/DMA_project1/Project1_dataset'+'/'+'user.csv'

    with open(filepath, 'r', encoding='utf-8') as csv_data:
        data_to_insert = []
        for row in csv_data.readlines()[1:]:
            row = row.strip().split(',')
            formatted_row = []

            for idx, data in enumerate(row):
                if data == '':
                    formatted_row.append(None)  # None을 사용하여 NULL 대체
                elif idx in [0]:
                    formatted_row.append(int(data))
                else:
                    formatted_row.append(data)

            data_to_insert.append(tuple(formatted_row))

    insert_query = "INSERT INTO USER (Uid, Unickname) VALUES (%s, %s)"
    cursor.executemany(insert_query, data_to_insert)
    cnx.commit()

    print("Data inserted successfully!")

    # TODO: WRITE CODE HERE
    cursor.close()


# Requirement3: insert data
def requirement3(host, user, password, directory):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Inserting data...")

    # TODO: WRITE CODE HERE

    # TODO: WRITE CODE HERE
    cursor.close()


# Requirement4: add constraint (foreign key)
def requirement4(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Adding constraints...")

    # TODO: WRITE CODE HERE

    # TODO: WRITE CODE HERE
    cursor.close()


# TODO: REPLACE THE VALUES OF FOLLOWING VARIABLES
host = "localhost"
user = "root"
password = "m@ysh201836"
directory_in = ""


requirement1(host=host, user=user, password=password)
requirement2(host=host, user=user, password=password)
'''
requirement3(host=host, user=user, password=password, directory=directory_in)
requirement4(host=host, user=user, password=password)
print("Done!")'''
