import pandas as pd
import re

def normalize_emp_id(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.upper()
    digits = s.str.extract(r"(\d+)", expand=False)
    return digits.apply(lambda x: f"EMP{str(x).zfill(4)}" if pd.notna(x) else pd.NA)

def null_emp_id(series: pd.Series) -> pd.Series:
    mask = series.isna()
    if mask.any():
        pd.DataFrame({"emp_id_null": series[mask]}).to_csv("data/null_id.csv", index=False)
    return series

def fix_duplicate_emp_id(series: pd.Series) -> pd.Series:
    mask = series.duplicated(keep=False)
    if mask.any():
        pd.DataFrame({"emp_id_duplicate": series[mask]}).to_csv("data/duplicated_id.csv", index=False)
    return series

#name
def fix_name(series: pd.Series) -> pd.Series:
    s = series.astype(str)
    s = s.str.replace(r"[^a-zA-Z ]", "", regex=True)
    return s.str.slice(0, 20)

def null_name(series: pd.Series) -> pd.Series:
    mask = series.isna()
    if mask.any():
        pd.DataFrame({"name_null": series[mask]}).to_csv("data/null_name.csv", index=False)
    return series

#age
def fix_age(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce").round()
    return s.where(s.between(18, 65))

def null_age(series: pd.Series) -> pd.Series:
    mask = series.isna()
    if mask.any():
        pd.DataFrame({"age_null": series[mask]}).to_csv("data/null_age.csv", index=False)
    return series

#email
def normalize_email(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.strip().str.lower()
    s = s.str.replace(" ", "", regex=False)
    return s.str.replace("..", ".", regex=False)

def null_email(series: pd.Series) -> pd.Series:
    mask = series.isna()
    if mask.any():
        pd.DataFrame({"email_null": series[mask]}).to_csv("data/null_email.csv", index=False)
    return series

#salary
def salary_remove_non_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")

def fix_salary(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce")
    return s.where(s.between(3000, 1000000))

#department
def normalize_department(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.upper()
