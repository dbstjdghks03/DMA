import mysql.connector
import csv
import pandas as pd

team = 0


def requirement1(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')

    # TODO: WRITE CODE HERE
    print('Creating schema...')
    cursor.execute('DROP DATABASE IF EXISTS DMA_team%02d;' % team)
    cursor.execute('CREATE DATABASE IF NOT EXISTS DMA_team%02d;' % team)

    # TODO: WRITE CODE HERE
    cursor.close()


def requirement2(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')

    # TODO: WRITE CODE HERE
    print('Creating tables...')
    cursor.execute('USE DMA_team%02d;' % team)

    # user
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    id INT(11) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')
    
    # follow
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS follow(
    follower_id INT(11) NOT NULL,
    followee_id INT(11) NOT NULL,
    PRIMARY KEY (follower_id, followee_id) );
    ''')
    
    #seller
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seller(
    id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')
    
    # seller_user
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seller_user(
    user_id INT(11) NOT NULL,
    seller_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id, seller_id) );
    ''')

    # cs_team
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cs_team(
    seller_id VARCHAR(255) NOT NULL,
    cs_phone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (seller_id, cs_phone, email) );
    ''')

    # category
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS category(
    id INT(11) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')
    
    # brand
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brand(
    id INT(11) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')
    
    # brand_seller
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brand_seller(
    brand_id INT(11) NOT NULL,
    seller_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (brand_id, seller_id) );
    ''')

    # product
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS product(
    id INT(11) NOT NULL,
    name VARCHAR(255) NOT NULL,
    selling_price INT(11) NOT NULL,
    original_price INT(11) NOT NULL,
    refund_fee INT(11) NOT NULL,
    exchange_fee INT(11) NOT NULL,
    brand_id INT(11) NOT NULL,
    category_id INT(11) NOT NULL,
    seller_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')
    
    #scrap
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scrap(
    user_id INT(255) NOT NULL,
    product_id INT(11) NOT NULL,
    PRIMARY KEY (user_id, product_id) );
    ''')

    # review
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS review(
    id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    user_id INT(11) NOT NULL,
    created_at DATETIME NOT NULL,
    comment VARCHAR(255) NOT NULL,
    overall_rating DECIMAL(11) NOT NULL,
    cost_rating DECIMAL(11) NOT NULL,
    delivery_rating DECIMAL(11) NOT NULL,
    design_rating DECIMAL(11) NOT NULL,
    durability_rating DECIMAL(11) NOT NULL,
    PRIMARY KEY (id) );
    ''')

    # delivery_method
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS delivery_method(
    id INT(11) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id) );
    ''')

    # product_delivery
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_delivery(
    product_id INT(11) NOT NULL,
    delivery_method_id INT(11) NOT NULL,
    is_free_delivery TINYINT(1) NOT NULL,
    is_overseas_purchase TINYINT(1) NOT NULL,
    is_departure_today TINYINT(1) NOT NULL,
    PRIMARY KEY (product_id, delivery_method_id) );
    ''')

    # TODO: WRITE CODE HERE
    cursor.close()


# Requirement3: insert data
def requirement3(host, user, password, directory):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')

    # TODO: WRITE CODE HERE
    print('Inserting data...')
    cursor.execute('USE DMA_team%02d;' % team)


    table_name = ['user', 'follow', 'seller', 'seller_user', 'cs_team','category', 
                  'brand', 'brand_seller', 'product', 'scrap', 'review',
                  'delivery_method','product_delivery']

    for table in table_name:
        print(table)
        filepath = directory + '/' + table + '.csv'

        f = open(filepath)
        csv_data = csv.reader(f)
        with open(filepath, 'r', encoding = 'utf-8-sig') as csv_data:
            next(csv_data, None)  # skip the headers
            
            for row in csv_data:
                try:
                    row = row.strip().split(sep=',')
                    # Change the null data
                    if '' in row:
                        temp = []
                        for item in row:
                            if item == '':
                                item = None
                            temp.append(item)
                        row = temp
                    if table in ['user', 'follow', 'seller_user', 'category', 'brand', 'brand_seller',
                     'scrap', 'delivery_method']:
                        cursor.execute('INSERT INTO ' + table + ' VALUES (%s,%s)', row)
                    elif table in ['seller', 'cs_team']:
                        cursor.execute('INSERT INTO ' + table + ' VALUES (%s,%s,%s)', row)
                    elif table in ['product_delivery']:
                        cursor.execute('INSERT INTO ' + table + ' VALUES (%s,%s,%s,%s,%s)', row)
                    elif table in ['product']:
                        cursor.execute('INSERT INTO ' + table + ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
                    elif table in ['review']:
                        cursor.execute('INSERT INTO ' + table + ' VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)

                    cnx.commit()
                except:
                    print(row)
    # TODO: WRITE CODE HERE
    cursor.close()


# Requirement4: add constraint (foreign key)
def requirement4(host, user, password):
    cnx = mysql.connector.connect(host=host, user=user, password=password)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')

    # TODO: WRITE CODE HERE
    print('Adding constraints...')
    cursor.execute('USE DMA_team%02d;' % team)

    cursor.execute('ALTER TABLE follow ADD CONSTRAINT FOREIGN KEY (follower_id) REFERENCES user(id);')
    print("constraint 1 added")

    cursor.execute('ALTER TABLE follow ADD CONSTRAINT FOREIGN KEY (followee_id) REFERENCES user(id);')
    print("constraint 2 added")

    cursor.execute('ALTER TABLE seller_user ADD CONSTRAINT FOREIGN KEY (seller_id) REFERENCES seller(id);')
    print("constraint 3 added")

    cursor.execute('ALTER TABLE seller_user ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES user(id);')
    print("constraint 4 added")

    cursor.execute('ALTER TABLE cs_team ADD CONSTRAINT FOREIGN KEY (seller_id) REFERENCES seller(id);')
    print("constraint 5 added")

    cursor.execute('ALTER TABLE brand_seller ADD CONSTRAINT FOREIGN KEY (brand_id) REFERENCES brand(id);')
    print("constraint 6 added")

    cursor.execute('ALTER TABLE brand_seller ADD CONSTRAINT FOREIGN KEY (seller_id) REFERENCES seller(id);')
    print("constraint 7 added")

    cursor.execute('ALTER TABLE product ADD CONSTRAINT FOREIGN KEY (brand_id) REFERENCES brand(id);')
    print("constraint 8 added")

    cursor.execute('ALTER TABLE product ADD CONSTRAINT FOREIGN KEY (category_id) REFERENCES category(id);')
    print("constraint 9 added")

    cursor.execute('ALTER TABLE product ADD CONSTRAINT FOREIGN KEY (seller_id) REFERENCES seller(id);')
    print("constraint 10 added")

    cursor.execute('ALTER TABLE scrap ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES user(id);')
    print("constraint 11 added")

    cursor.execute('ALTER TABLE scrap ADD CONSTRAINT FOREIGN KEY (product_id) REFERENCES product(id);')
    print("constraint 12 added")

    cursor.execute('ALTER TABLE review ADD CONSTRAINT FOREIGN KEY (product_id) REFERENCES product(id);')
    print("constraint 13 added")

    cursor.execute('ALTER TABLE review ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES user(id);')
    print("constraint 14 added")

    cursor.execute('ALTER TABLE product_delivery ADD CONSTRAINT FOREIGN KEY (product_id) REFERENCES product(id);')
    print("constraint 15 added")

    cursor.execute('ALTER TABLE product_delivery ADD CONSTRAINT FOREIGN KEY (delivery_method_id) REFERENCES delivery_method(id);')
    print("constraint 16 added")
    # TODO: WRITE CODE HERE
    cursor.close()

# TODO: REPLACE THE VALUES OF FOLLOWING VARIABLES
host = 'localhost'
user = 'root'
password = ''
directory_in = ''

if __name__ == '__main__':
    requirement1(host=host, user=user, password=password)
    requirement2(host=host, user=user, password=password)
    requirement3(host=host, user=user, password=password, directory=directory_in)
    requirement4(host=host, user=user, password=password)
    print('Done!')


