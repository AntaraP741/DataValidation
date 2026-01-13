# Data Validation Framework (Python + Pandera)

This project implements a **production-style data validation pipeline** for structured datasets using Python, Pandas, and Pandera. It demonstrates how raw data can be normalized, validated against a schema, checked against business rules, and separated into clean and rejected records with full auditability.

The design follows real-world **ETL and data quality engineering** patterns used in fintech, retail, and analytics platforms.

---

## Architecture

The framework is built in four layers:

```
Raw Data
   ↓
Normalizer  → cleans and standardizes values
   ↓
Schema      → enforces column types and nullability (Pandera)
   ↓
Rules       → enforces business constraints
   ↓
Validator   → produces clean and rejected datasets
```

Each layer has a single responsibility, making the system reusable, testable, and scalable.

---

## Project Structure

```
validation_pandera/
│
├── data/
│   ├── raw_employees.csv
│   ├── cleaned_employees.csv
│   └── rejected_employees.csv
│
├── validation/
│   ├── __init__.py
│   ├── schema.py
│   ├── normalizer.py
│   ├── rules.py
│   └── validator.py
│
├── tests/
│   └── test_validator.py
│
└── main.py
```

---

## Data Schema

The project validates an employee dataset with the following structure:

| Column     | Type    | Description                     |
| ---------- | ------- | ------------------------------- |
| emp_id     | string  | Employee ID in format `EMP####` |
| name       | string  | Alphabetic name (max 20 chars)  |
| age        | integer | Between 18 and 65               |
| email      | string  | Valid email address             |
| salary     | float   | Positive salary                 |
| department | string  | One of `HR, IT, SALES, FINANCE` |

---

## What the Framework Does

1. **Normalization**

   * Standardizes formats (case, whitespace, numeric conversion)
   * Converts invalid values to `NaN`
   * Preserves original raw values for audit

2. **Schema Validation**

   * Enforces column presence, data types, and nullability using Pandera

3. **Business Rules**

   * Validates patterns (EMP ID format, email format)
   * Enforces ranges (age, salary)
   * Enforces allowed categories (department)
   * Enforces uniqueness (emp_id, email)

4. **Validation Engine**

   * Combines all checks
   * Splits data into:

     * `cleaned_employees.csv`
     * `rejected_employees.csv`

---

## How to Run

### 1. Install dependencies

```
pip install pandas pandera pytest
```

### 2. Run validation on real data

```
python main.py
```

This will generate:

* `data/cleaned_employees.csv`
* `data/rejected_employees.csv`

---

## How to Run Unit Tests

From the project root:

```
set PYTHONPATH=.
pytest
```

All tests should pass, verifying that:

* Invalid ages are rejected
* Invalid IDs are rejected
* Negative salaries are rejected
* Only fully valid rows pass

---

If you want, I can also provide a **short “How this works” section for interview use** that you can add to the README.
