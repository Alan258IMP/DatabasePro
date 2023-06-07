import pandas as pd
import yaml
import psycopg2
import sqlalchemy as sa

class DatabaseConnector:
    def __init__(self):
        self.read_db_creds()
        self.init_db_engine()

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as creds:
            self.creds = yaml.safe_load(creds)
            psycopg2.connect(host = self.creds['RDS_HOST'], user = self.creds['RDS_USER'], password = self.creds['RDS_PASSWORD'], dbname = self.creds['RDS_DATABASE'], port = 5432)

    def init_db_engine(self):
        # TODO: Connect credentials, set Github secrets
        self.engine = sa.create_engine(f"{'postgresql'}+{'DBAPI'}://{self.creds['RDS_USER']}:{self.creds['RDS_PASSWORD']}@{self.creds['RDS_HOST']}:{self.creds['RDS_PORT']}/{self.creds['RDS_DATABASE']}")
        self.engine.connect()

    def upload_to_db(self, df, table_name):
        '''
        Uploads a pandas dataframe to a PostgreSQL database table.

        Parameters
        ----------
        df
            a pandas DataFrame containing the data to be uploaded to the database
        table
            The name of the table in the database where the data will be uploaded.
        '''
        database_type = 'postgresql'
        DBAPI = 'psycopg2'
        # credentials to be edited
        HOST = 'localhost' 
        USER = 'postgres' 
        PASSWORD = 'AlanLi258'
        DATABASE = 'sales_data'
        PORT = 5432
        self.sql_engine = sa.create_engine(f"{database_type}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        #with self.sql_engine.connect().execution_options(autocommit=True) as conn:
        #    df.to_sql(table_name, con = conn, if_exists = 'replace', index = False)


