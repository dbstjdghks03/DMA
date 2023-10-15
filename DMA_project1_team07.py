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
            PRIMARY KEY (id)
        );
        """
    )
    # 데이터상 nickname도 not null이긴 함

    # seller
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seller(
            id VARCHAR(255) NOT NULL,
            name VARCHAR(255),
            address VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )
    # 데이터상 다 not null

    # seller_user
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS seller_user(
            user_id INT(11) NOT NULL,
            seller_id VARCHAR(255) NOT NULL,
            PRIMARY KEY (user_id, seller_id)
        );
        """
    )
    # 데이터상 다 not null

    # review
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS review(
            id INT(11) NOT NULL,
            product_id INT(11) NOT NULL,
            user_id INT(11) NOT NULL,
            created_at DATETIME,
            comment VARCHAR(255),
            overall_rating DECIMAL(11),
            cost_rating DECIMAL(11),
            delivery_rating DECIMAL(11),
            design_rating DECIMAL(11),
            durability_rating DECIMAL(11),
            PRIMARY KEY (id)
        );
        """
    )

    # scrap
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS scrap(
            user_id INT(11) NOT NULL,
            product_id INT(11) NOT NULL,
            PRIMARY KEY (user_id, product_id)
        );
        """
    )

    # product
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product(
            id INT(11) NOT NULL,
            name VARCHAR(255),
            selling_price INT(11),
            original_price INT(11),
            refund_fee INT(11),
            exchange_fee INT(11),
            brand_id INT(11),
            category_id INT(11),
            seller_id VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )

    # product_delivery
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product_delivery(
            product_id INT(11) NOT NULL,
            delivery_method_id INT(11) NOT NULL,
            is_free_delivery TINYINT(1),
            is_overseas_purchase TINYINT(1),
            is_departure_today TINYINT(1),
            PRIMARY KEY(product_id, delivery_method_id)
        );
        """
    )

    # delivery_method
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS delivery_method(
            id INT(11) NOT NULL,
            name VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )

    # follow
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS follow(
            follower_id INT(11) NOT NULL,
            followee_id INT(11) NOT NULL,
            PRIMARY KEY (follower_id, followee_id)
        );
        """
    )

    # cs_team
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cs_team(
            seller_id VARCHAR(255) NOT NULL,
            cs_phone VARCHAR(255),
            email VARCHAR(255),
            PRIMARY KEY (seller_id, cs_phone, email)
        );
        """
    )

    # category
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category(
            id INT(11) NOT NULL,
            name VARCHAR(255),
            PRIMARY KEY (id)
        );
        """
    )

    # brand_seller
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS brand_seller(
            brand_id INT(11) NOT NULL,
            seller_id VARCHAR(255) NOT NULL,
            PRIMARY KEY (brand_id, seller_id)
        );
        """
    )
    # brand
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS brand(
            id INT(11) NOT NULL,
            name VARCHAR(255),
            PRIMARY KEY (id)
        );
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
        def __init__(
            self,
            file_name,
            integer_attribute_index_list,
            float_attribute_index_list,
            insert_sql,
        ):
            self.file_path = directory + file_name
            self.integer_attribute_index_list = integer_attribute_index_list
            self.float_attribute_index_list = float_attribute_index_list
            self.insert_sql = insert_sql

        def load_data(self):
            with open(self.file_path, "r", encoding="utf-8") as csv_data:
                tuples_to_insert = []
                count = 0
                for row in csv_data.readlines()[1:]:
                    row = row.strip().split(",")

                    formatted_row = []
                    for idx, data in enumerate(row):
                        if data == "":
                            formatted_row.append(None)  # None을 사용하여 NULL 대체
                        elif idx in self.integer_attribute_index_list:
                            formatted_row.append(int(data))
                        elif idx in self.float_attribute_index_list:
                            formatted_row.append(float(data))
                        else:
                            formatted_row.append(data)

                    # cursor.execute(self.insert_sql, tuple(formatted_row))

                    tuples_to_insert.append(tuple(formatted_row))
                    count += 1
                    if count % 1000 == 0:
                        cursor.executemany(self.insert_sql, tuples_to_insert)
                        tuples_to_insert = []
                        cnx.commit()

    insertion_data = [
        ("user.csv", [0], [], "INSERT INTO user (id, nickname) VALUES (%s, %s);"),
        (
            "seller.csv",
            [],
            [],
            "INSERT INTO seller (id, Name, address) VALUES (%s, %s, %s);",
        ),
        (
            "seller_user.csv",
            [0],
            [],
            "INSERT INTO seller_user (user_id, seller_id) VALUES (%s, %s);",
        ),
        (
            "review.csv",
            [0, 1, 2],
            [5, 6, 7, 8, 9],
            """
            INSERT INTO review (id, product_id, user_id, created_at, comment, overall_rating,
            cost_rating, delivery_rating, design_rating, durability_rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
        ),
        (
            "scrap.csv",
            [0, 1],
            [],
            "INSERT INTO scrap (user_id, product_id) VALUES (%s, %s);",
        ),
        (
            "product.csv",
            [0, 2, 3, 4, 5, 6, 7],
            [],
            """INSERT INTO product (id, name, selling_price, original_price, refund_fee, exchange_fee,
            brand_id, category_id, seller_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
        ),
        (
            "product_delivery.csv",
            [0, 1, 2, 3, 4],
            [],
            """INSERT INTO product_delivery (product_id, delivery_method_id,
            is_free_delivery, is_overseas_purchase, is_departure_today)
            VALUES (%s, %s, %s, %s, %s);""",
        ),
        (
            "delivery_method.csv",
            [0],
            [],
            "INSERT INTO delivery_method (id, name) VALUES (%s, %s);",
        ),
        (
            "follow.csv",
            [0, 1],
            [],
            "INSERT INTO follow (follower_id, followee_id) VALUES (%s, %s);",
        ),
        (
            "cs_team.csv",
            [],
            [],
            "INSERT INTO cs_team (seller_id, cs_phone, email) VALUES (%s, %s, %s);",
        ),
        (
            "category.csv",
            [0],
            [],
            "INSERT INTO category (id, name) VALUES (%s, %s);",
        ),
        (
            "brand_seller.csv",
            [0],
            [],
            "INSERT INTO brand_seller (brand_id, seller_id) VALUES (%s, %s);",
        ),
        (
            "brand.csv",
            [0],
            [],
            "INSERT INTO brand (id, name) VALUES (%s, %s);",
        ),
    ]

    for data in insertion_data:
        table_loader = TableLoader(*data)
        table_loader.load_data()

    # 잘 들어갔는지 테스트용
    # cursor.execute("SELECT * FROM review;")
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
