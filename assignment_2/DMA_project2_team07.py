# TODO: CHANGE THIS FILE NAME TO DMA_project2_team##.py
# EX. TEAM 1 --> DMA_project2_team01.py

# TODO: IMPORT LIBRARIES NEEDED FOR PROJECT 2
import mysql.connector
import os
import csv
import surprise
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import KFold
from surprise.model_selection.search import GridSearchCV
from collections import defaultdict
import numpy as np
import pandas as pd
from sklearn import tree
import graphviz

from mlxtend.frequent_patterns import association_rules, apriori

np.random.seed(0)

# TODO: CHANGE GRAPHVIZ DIRECTORY
# If you installed graphviz with the command conda install python-graphviz at the anaconda prompt, you would not need the following procedure.
# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz2.47.1/bin/'
# os.environ["PATH"] += os.pathsep + '/usr/local/Cellar/graphviz/2.47.1/bin/'  # for MacOS



# TODO: CHANGE MYSQL INFORMATION, team number
HOST = 'localhost'
USER = 'root'
PASSWORD = ''
SCHEMA = ''
team = 

# PART 1: Decision tree 
def part1():
    cnx = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port = 3306)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')
    cursor.execute('USE %s;' % SCHEMA)

    # TODO: Requirement 1-1. MAKE best_item column
    
    # TODO: Requirement 1-1.

    
    # TODO: Requirement 1-2. WRITE MYSQL QUERY AND EXECUTE. SAVE to .csv file
    
    # TODO: Requirement 1-2.

    
    # TODO: Requirement 1-3. MAKE AND SAVE DECISION TREE
    # gini file name: DMA_project2_team##_part1_gini.pdf
    # entropy file name: DMA_project2_team##_part1_entropy.pdf

    # TODO: Requirement 1-3.

    
    # TODO: Requirement 1-4. Don't need to append code for 1-4
    cursor.close()

    
# PART 2: Association analysis
def part2():
    cnx = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, port = 3306)
    cursor = cnx.cursor()
    cursor.execute('SET GLOBAL innodb_buffer_pool_size=2*1024*1024*1024;')
    cursor.execute('USE %s;' % SCHEMA)

    # TODO: Requirement 2-1. CREATE VIEW AND SAVE to .csv file
    
    # TODO: Requirement 2-1.

    
    # TODO: Requirement 2-2. CREATE 2 VIEWS AND SAVE partial one to .csv file

    # TODO: Requirement 2-2.

    
    # TODO: Requirement 2-3. MAKE HORIZONTAL VIEW
    # file name: DMA_project2_team##_part2_horizontal.pkl
    
    # TODO: Requirement 2-3.

    
    # TODO: Requirement 2-4. ASSOCIATION ANALYSIS
    # filename: DMA_project2_team##_part2_association.pkl (pandas dataframe)
    
    # TODO: Requirement 2-4.
    cursor.close()


# TODO: assign product_file_path with path of 'product.csv'
def get_name_of_product(pid):
    product_file_path = ''
    product_list = pd.read_csv(product_file_path,dtype=object)
    return product_list[product_list['id']==pid].values[0][1]


# TODO: Requirement 3-1. WRITE get_top_n
def get_top_n(algo, testset, id_list, n, user_based=True):
    results = defaultdict(list)
    testset = list(filter(lambda x: len(x[1]) < 9, testset))
    testset_id = []
    if user_based:
        # TODO: testset의 데이터 중에 user id가 id_list 안에 있는 데이터만 따로 testset_id로 저장
        # Hint: testset은 (user_id, product_id, default_rating)의 tuple을 요소로 갖는 list
        
        # TODO
        
        predictions = algo.test(testset_id)
        for uid, pid, true_r, est, _ in predictions:
            # TODO: results는 user_id를 key로,  [(product_id, estimated_rating)의 tuple이 모인 list]를 value로 갖는 dictionary
            
            # TODO
    else:
        # TODO: testset의 데이터 중 product id가 id_list 안에 있는 데이터만 따로 testset_id라는 list로 저장
        # Hint: testset은 (user_id, product_id, default_rating)의 tuple을 요소로 갖는 list
        
        # TODO
        
        predictions = algo.test(testset_id)
        for uid, pid, true_r, est, _ in predictions:
            # TODO: results는 product_id를 key로, [(user_id, estimated_rating)의 tuple이 모인 list]를 value로 갖는 dictionary
            
            # TODO

    for id_, ratings in results.items():
        # TODO: rating 순서대로 정렬하고 top-n개만 유지
        
        # TODO

    return results


# PART 3. Requirement 3-2, 3-3, 3-4
def part3():
    # TODO: assign file_path with path of 'rating.csv'
    file_path = ''
    reader = Reader(line_format='user item rating', sep=',', rating_scale=(0.5, 5.0), skip_lines=1)
    data = Dataset.load_from_file(file_path, reader=reader)

    trainset = data.build_full_trainset()
    testset = trainset.build_anti_testset()

    uid_list = ['2996825', '351451', '1595159', '18143238', '3997100']
    # TODO - set algorithm for 3-2-1
    algo =
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-2-1.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-2-1 ended')

    # TODO - set algorithm for 3-2-2
    algo =
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-2-2.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-2-2 ended')

    # TODO - 3-2-3. Best Model
    best_algo_ub = 
    # TODO

    
    pid_list = ['1795704', '1160354', '768611', '817168', '1131072']       
    # TODO - set algorithm for 3-3-1
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, pid_list, n=10, user_based=False)
    with open('3-3-1.txt', 'w') as f:
        for pid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('Product name %s top-10 results\n' % get_name_of_product(pid))
            for uid, score in ratings:
                f.write('User ID %s\n\tscore %s\n' % (uid, str(score)))
            f.write('\n')
    print('3-3-1 ended')

    # TODO - set algorithm for 3-3-2
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, pid_list, n=10, user_based=False)
    with open('3-3-2.txt', 'w') as f:
        for pid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('Product name %s top-10 results\n' % get_name_of_product(pid))
            for uid, score in ratings:
                f.write('User ID %s\n\tscore %s\n' % (uid, str(score)))
            f.write('\n')
    print('3-3-2 ended')

    # TODO - 3-3-3. Best Model
    best_algo_ib = 
    # TODO


    # TODO - set algorithm for 3-4-1
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-4-1.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-4-1 ended')

    # TODO - set algorithm for 3-4-2
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-4-2.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-4-2 ended')

    # TODO - set algorithm for 3-4-3
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-4-3.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-4-3 ended')

    # TODO - set algorithm for 3-4-4
    algo = 
    # TODO
    
    algo.fit(trainset)
    results = get_top_n(algo, testset, uid_list, n=5, user_based=True)
    with open('3-4-4.txt', 'w') as f:
        for uid, ratings in sorted(results.items(), key=lambda x: x[0]):
            f.write('User ID %s top-5 results\n' % uid)
            for pid, score in ratings:
                f.write('Product name %s\n\tscore %s\n' % (get_name_of_product(pid), str(score)))
            f.write('\n')
    print('3-4-4 ended')

    # TODO - 3-4-5. Best Model
    best_algo_mf = 
    # TODO
        

if __name__ == '__main__':
    part1()
    part2()
    part3()
