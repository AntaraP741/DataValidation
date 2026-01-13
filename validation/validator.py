import pandas as pd
from validation.schema import schema
import validation.rules as rules
import validation.normalizer as normalizer


def run_validation(df: pd.DataFrame):
    raw_df = df.copy()
    df = df.copy()

    df["emp_id"] = normalizer.normalize_emp_id(df["emp_id"])
    df["name"] = normalizer.fix_name(df["name"])
    df["age"] = normalizer.fix_age(df["age"])
    df["email"] = normalizer.normalize_email(df["email"])
    df["salary"] = normalizer.fix_salary(df["salary"])
    df["department"] = normalizer.normalize_department(df["department"])

    try:
        schema.validate(df, lazy=True)
        schema_mask = pd.Series(True, index=df.index)
    except Exception as e:
        failure_df = e.failure_cases
        schema_mask = ~df.index.isin(failure_df["index"])

    emp_id_mask = (
        df["emp_id"].notna()
        & rules.check_emp_id(df["emp_id"])
        & rules.check_emp_id_unique(df["emp_id"])
    )

    name_mask = df["name"].notna() & rules.check_name(df["name"])

    age_mask = df["age"].notna() & rules.check_age(df["age"])

    email_mask = (
        df["email"].notna()
        & rules.check_email(df["email"])
        & rules.check_email_unique(df["email"])
    )

    salary_mask = df["salary"].notna() & rules.check_salary(df["salary"])

    dept_mask = df["department"].notna() & rules.check_department(df["department"])

    final_mask = (
        schema_mask
        & emp_id_mask
        & name_mask
        & age_mask
        & email_mask
        & salary_mask
        & dept_mask
    )

    clean_df = raw_df[final_mask]
    rejected_df = raw_df[~final_mask]


    return clean_df, rejected_df
