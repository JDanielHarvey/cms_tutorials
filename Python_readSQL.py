import pyodbc
from sqlalchemy import create_engine
import pandas as pd

SERVER = '54.187.115.114'
UN = 'sqluser_FRATMEN'
PW = '8UUw7^gHHw3w3lxxx0o0'
DRIVER = 'SQL Server Native Client 11.0'
DB = 'Fratmen'

engine = create_engine(f'mssql+pyodbc://{UN}:{PW}@{SERVER}/{DB}?driver={DRIVER}')
connection = engine.connect()
