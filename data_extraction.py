import numpy as np
import pandas as pd
import json
import requests
import sqlalchemy as sa
from tabula import read_pdf

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
    
    def retrieve_pdf_data(self, src):
        df = read_pdf(src, pages='all') # "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        data = pd.concat(df, ignore_index=True)
        df2 = pd.DataFrame(data)
        return df2

if __name__ == "__main__":
    connector = DatabaseConnector()       
    extractor = DataExtractor()
    cleaner = DataCleaner()