import pandas as pd

def check_emp_id(series: pd.Series) -> pd.Series:
    pattern = r"^EMP[0-9]{4}$"
    return series.astype(str).str.match(pattern)

def check_emp_id_unique(series: pd.Series) -> pd.Series:
    return ~series.duplicated(keep=False)

def check_name(series: pd.Series) -> pd.Series:
    pattern = r"^[A-Za-z ]{1,20}$"
    return series.astype(str).str.match(pattern)

def check_age(series: pd.Series) -> pd.Series:
    return series.between(18, 65)

def check_email(series: pd.Series) -> pd.Series:
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    return series.astype(str).str.match(pattern)

def check_email_unique(series: pd.Series) -> pd.Series:
    return ~series.duplicated(keep=False)

def check_salary(series: pd.Series) -> pd.Series:
    return series.gt(0)

def check_department(series: pd.Series) -> pd.Series:
    allowed = ["HR", "IT", "SALES", "FINANCE"]
    return series.isin(allowed)
