# import csv

import mysql.connector

# TODO: REPLACE THE VALUE OF VARIABLE team (EX. TEAM 1 --> team = 1)
team = 7


# Requirement1: create schema ( name: DMA_team## )
def requirement1(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Creating schema...")

    # TODO: WRITE CODE HERE
    # TODO: 삭제할 부분
    cursor.execute("DROP DATABASE DMA_team07;")
    cnx.commit()
    # TODO: 삭제할 부분
    cursor.execute("CREATE DATABASE IF NOT EXISTS DMA_team07;")
    # TODO: WRITE CODE HERE
    cursor.close()


# Requierement2: create table
def requirement2(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Creating tables...")

    # TODO: WRITE CODE HERE
    cursor.execute("USE DMA_team07;")

    # user
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
        id INT(11) NOT NULL,
        nickname VARCHAR(255),
        PRIMARY KEY (id));
        """
    )
    # seller
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seller(
        id VARCHAR(255) NOT NULL,
        Name VARCHAR(255),
        address VARCHAR(255),
        PRIMARY KEY (id));
        """
    )
    # seller_user
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seller_user(
        user_id INT(11) NOT NULL,
        seller_id VARCHAR(255) NOT NULL);
        """
    )
    # TODO: WRITE CODE HERE
    cursor.close()


# Requirement3: insert data
def requirement3(host, user, password, directory):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;")
    print("Inserting data...")

    # TODO: WRITE CODE HERE
    cursor.execute("USE DMA_team07;")

    class TableLoader:
        def __init__(self, file_name, integer_attribute_index_list, insert_sql):
            self.file_path = directory + file_name
            self.integer_attribute_index_list = integer_attribute_index_list
            self.insert_sql = insert_sql

        def load_data(self):
            # load data
            with open(self.file_path, "r", encoding="utf-8") as csv_data:
                tuples_to_insert = []
                for row in csv_data.readlines()[1:]:
                    row = row.strip().split(",")

                    formatted_row = []
                    for idx, data in enumerate(row):
                        if data == "":
                            formatted_row.append(None)  # None을 사용하여 NULL 대체
                        elif idx in self.integer_attribute_index_list:
                            formatted_row.append(int(data))
                        else:
                            formatted_row.append(data)

                    tuples_to_insert.append(tuple(formatted_row))

            cursor.executemany(self.insert_sql, tuples_to_insert)
            cnx.commit()

    insertion_data = [
        ("user.csv", [0], "INSERT INTO user (id, nickname) VALUES (%s, %s) ;"),
        (
            "seller.csv",
            [],
            "INSERT INTO seller (id, Name, address) VALUES (%s, %s, %s) ;",
        ),
        (
            "seller_user.csv",
            [0],
            "INSERT INTO seller_user (user_id, seller_id) VALUES (%s, %s) ;",
        ),
    ]

    for file_name, integer_attribute_index_list, insert_sql in insertion_data:
        table_loader = TableLoader(file_name, integer_attribute_index_list, insert_sql)
        table_loader.load_data()

    # 잘 들어갔는지 테스트용
    # cursor.execute("SELECT * FROM seller;")
    # for row in cursor:
    #     print(row)

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
password = ""
directory_in = "./Project1_dataset/"


requirement1(host=host, user=user, password=password)
requirement2(host=host, user=user, password=password)
requirement3(host=host, user=user, password=password, directory=directory_in)
# requirement4(host=host, user=user, password=password)
# print("Done!")
