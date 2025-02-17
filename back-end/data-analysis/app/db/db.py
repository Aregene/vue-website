'''
Date: 2025-02-16 12:43:32
LastEditors: Aregene
LastEditTime: 2025-02-16 13:26:35
'''
#app.db.db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from dotenv import load_dotenv
import os
from app.models.data_model import Data

def get_db_url():
    # 加载 .env 文件
    load_dotenv()
        # 数据库连接URL
    DATABASE_URL = os.getenv('DATABASE_URL')
    return DATABASE_URL


def db_session(url):
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# 连接数据库



def read_and_store_excel(session):
    # 获取当前目录和文件路径
    current_dir = os.path.dirname(__file__)
    file_path_data = os.path.join(current_dir, '..', 'resource', 'data.xlsx')
    
    # 读取Excel文件
    try:
        data_df = pd.read_excel(file_path_data)
        
        # 将data.xlsx数据插入data表
        for index, row in data_df.iterrows():
            data_entry = Data(
                a=int(row['a']),
                b=int(row['b']),
                c=int(row['c']),
                d=int(row['d']),
                e=int(row['e']),
                f=int(row['f']),
                g=int(row['g']),
                h=int(row['h']),
                i=int(row['i']),
                j=int(row['j']),
                k=int(row['k']),
            )
            session.add(data_entry)
        
        
        session.commit()
        print("Data stored successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

read_and_store_excel(db_session(get_db_url()))
# python -m app.db.db
# 输出：Data stored successfully.