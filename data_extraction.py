import numpy as np
import pandas as pd
import json
import requests
import sqlalchemy as sa

from database_utils import DatabaseConnector
from data_cleaning import DataCleaner

class DataExtractor:
    def __init__(self, **kwargs):
        pass

    def read_rds_table(self, engine, table_name):
        # dbname to be edited
        return pd.read_sql_table(table_name, engine) # engine = postgres:///db_name
    
    def list_db_tables(self):
        inspector = sa.inspect(self.engine)
        return inspector.get_table_names()

if __name__ == "__main__":
    connector = DatabaseConnector()       
    extractor = DataExtractor()
    cleaner = DataCleaner()