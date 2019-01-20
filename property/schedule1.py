# _*_ coding:utf-8 _*_ 

import warnings
import json

DB_NAME='data/schdule1_db'
CONRERENCE='conference.115'
JSON=u'../osconfeed.json'


class Record:

    def __init__(self,**kw):
        self.__dict__.update(kw)

    def __str__(self,):

        return json.dumps(self.__dict__)



def load_db(db):

    fp=open(JSON)
    raw_data=json.load(fp)
    # warnings.warn('load data from {}'.format(JSON))

    for collection,rec_list in raw_data['Schedule'].items():
        record_type=collection[:-1]
        for record in rec_list:

            key='{}.{}'.format(record_type,record['serial'])
            record['serial'] = key
            db[key]=Record(**record)

    return db



if __name__ =='__main__': 


    fp=open(JSON)
    raw_data=json.load(fp) 

    db={}
    load_db(db)

    print (db[CONRERENCE])
