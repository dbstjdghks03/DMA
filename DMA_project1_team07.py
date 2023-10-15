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
    cursor.execute("USE DMA_team07")

    cursor.execute("USE DMA_team07")

    class make_table:
        def __init__(self, cnx, cursor):
            self.cnx = cnx
            self.cursor = cursor
            self.file_doc = (
                "/Users/yunseonghwan/Desktop/2023-2/데이터 관리와 분석/DMA_project1/Project1_dataset"
                + "/"
            )
            self.files = {
                "user_path": self.file_doc + "user.csv",
                "seller_path": self.file_doc + "seller.csv",
                "seller_user_path": self.file_doc + "seller_user.csv",
                "review_path": self.file_doc + "review.csv",
                "scrap_path": self.file_doc + "scrap.csv",
                "product_path": self.file_doc + "product.csv",
                "product_delivery_path": self.file_doc + "product_delivery.csv",
                "delivery_method_path": self.file_doc + "delivery_method.csv",
                "follow_path": self.file_doc + "follow.csv",
                "cs_team_path": self.file_doc + "cs_team.csv",
                "category_path": self.file_doc + "category.csv",
                "brand_seller_path": self.file_doc + "brand_seller.csv",
                "brand_path": self.file_doc + "brand.csv",
            }
            self.user_table()
            self.seller_table()
            self.seller_user_table()

        def is_table_exists(self, table_name):
            self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = self.cursor.fetchone()
            return result is not None

        def user_table(self):
            exists = self.is_table_exists(table_name="user")
            if exists:
                return
            else:
                self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user(
                    id INT(11) NOT NULL,
                    nickname VARCHAR(255),
                    PRIMARY KEY (id)) ;
                    """
                )
                filepath = self.files["user_path"]

                with open(filepath, "r", encoding="utf-8") as csv_data:
                    data_to_insert = []
                    for row in csv_data.readlines()[1:]:
                        row = row.strip().split(",")
                        formatted_row = []

                        for idx, data in enumerate(row):
                            if data == "":
                                formatted_row.append(None)  # None을 사용하여 NULL 대체
                            elif idx in [0]:
                                formatted_row.append(int(data))
                            else:
                                formatted_row.append(data)

                        data_to_insert.append(tuple(formatted_row))

                insert_query = "INSERT INTO user (id, nickname) VALUES (%s, %s) ;"
                self.cursor.executemany(insert_query, data_to_insert)
                self.cnx.commit()
                return

        def seller_table(self):
            exists = self.is_table_exists(table_name="seller")
            if exists:
                return
            else:
                self.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS seller(
                    id VARCHAR(255) NOT NULL,
                    Name VARCHAR(255),
                    address VARCHAR(255),
                    PRIMARY KEY (id)) ;
                    """
                )
                filepath = self.files["seller_path"]

                with open(filepath, "r", encoding="utf-8") as csv_data:
                    data_to_insert = []
                    for row in csv_data.readlines()[1:]:
                        row = row.strip().split(",")
                        formatted_row = []

                        for idx, data in enumerate(row):
                            if data == "":
                                formatted_row.append(None)
                            else:
                                formatted_row.append(data)

                        data_to_insert.append(tuple(formatted_row))

                insert_query = (
                    "INSERT INTO seller (id, Name, address) VALUES (%s, %s, %s) ;"
                )
                self.cursor.executemany(insert_query, data_to_insert)
                self.cnx.commit()

        def seller_user_table(self):
            exists = self.is_table_exists(table_name="seller_user")
            if exists:
                return
            else:
                exists2 = self.is_table_exists(table_name="SELLER_USER_ID")
                if exists2:
                    return
                else:
                    self.cursor.execute(
                        """
                        CREATE TABLE IF NOT EXISTS SELLER_USER_ID (
                        SUIid INT(11) NOT NULL,
                        PRIMARY KEY (SUIid)) ;
                        """
                    )
                    filepath = self.files["seller_user_path"]
                    with open(filepath, "r", encoding="utf-8") as csv_data:
                        data_to_insert = set()
                        for row in csv_data.readlines()[1:]:
                            row = row.strip().split(",")
                            formatted_row = []

                            for idx, data in enumerate(row):
                                if data == "":
                                    formatted_row.append(None)
                                if idx in [0]:
                                    if int(data) in data_to_insert:
                                        pass
                                    formatted_row.append(int(data))

                            data_to_insert.add(tuple(formatted_row))

                    data_to_insert = list(data_to_insert)
                    insert_query = "INSERT INTO SELLER_USER_ID (SUIid) VALUES (%s) ;"
                    self.cursor.executemany(insert_query, data_to_insert)
                    self.cnx.commit()

                self.cursor.execute(
                    """
                        CREATE TABLE IF NOT EXISTS seller_user(
                        user_id INT(11) NOT NULL,
                        seller_id VARCHAR(255) NOT NULL) ;
                        """
                )
                filepath = self.files["seller_user_path"]
                with open(filepath, "r", encoding="utf-8") as csv_data:
                    data_to_insert = []
                    for row in csv_data.readlines()[1:]:
                        row = row.strip().split(",")
                        formatted_row = []

                        for idx, data in enumerate(row):
                            if data == "":
                                formatted_row.append(None)
                            elif idx in [0]:
                                formatted_row.append(int(data))
                            else:
                                formatted_row.append(data)

                        data_to_insert.append(tuple(formatted_row))

                insert_query = (
                    "INSERT INTO seller_user (user_id, seller_id) VALUES (%s, %s) ;"
                )
                self.cursor.executemany(insert_query, data_to_insert)
                self.cnx.commit()
                return

    make_table(cnx, cursor)

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
"""
requirement3(host=host, user=user, password=password, directory=directory_in)
requirement4(host=host, user=user, password=password)
print("Done!")"""
