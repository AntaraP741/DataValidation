import pandera as pd
from pandera import Column, DataFrameSchema, Check

schema = DataFrameSchema(
    columns = {
        "emp_id": Column(dtype = str, nullable = False),
        "name" : Column(dtype = str, nullable = False),
        "age" : Column(dtype = int),
        "email" : Column(dtype = str),
        "salary" : Column(dtype =float),
        "department" : Column(dtype = str)
        }
)