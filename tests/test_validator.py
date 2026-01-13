import pandas as pd
from validation.validator import run_validation


def get_test_dataframe():
    return pd.DataFrame({
        "emp_id": ["EMP1001", "emp1002", "badid", "EMP1004"],
        "name": ["John", "Alice", "Bob@", "Chris"],
        "age": [25, 17, 30, 40],
        "email": ["john@gmail.com", "alice@gmail.com", "bademail", "chris@gmail.com"],
        "salary": [50000, 40000, -100, 70000],
        "department": ["IT", "HR", "SALES", "BAD"]
    })


def test_only_valid_rows_pass():
    df = get_test_dataframe()

    clean, rejected = run_validation(df)

    assert len(clean) == 1
    assert clean.iloc[0]["emp_id"] == "EMP1001"


def test_invalid_age_is_rejected():
    df = get_test_dataframe()

    clean, rejected = run_validation(df)

    assert (rejected["age"] == 17).any()


def test_invalid_department_rejected():
    df = get_test_dataframe()

    clean, rejected = run_validation(df)

    assert (rejected["department"] == "BAD").any()


def test_invalid_emp_id_rejected():
    df = get_test_dataframe()

    clean, rejected = run_validation(df)

    assert (rejected["emp_id"] == "badid").any()


def test_salary_must_be_positive():
    df = get_test_dataframe()

    clean, rejected = run_validation(df)

    assert (rejected["salary"] < 0).any()
