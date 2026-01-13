import pandas as pd
from validation.validator import run_validation

def main():
    df = pd.read_csv("data/raw_employees.csv")

    clean, rejected = run_validation(df)

    clean.to_csv("data/cleaned_employees.csv", index=False)
    rejected.to_csv("data/rejected_employees.csv", index=False)

    print("Total rows:", len(df))
    print("Valid rows:", len(clean))
    print("Rejected rows:", len(rejected))

if __name__ == "__main__":
    main()
