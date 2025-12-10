import sqlite3
from pathlib import Path

import pandas as pd


def main() -> None:
    base_path = Path(__file__).parent

    # Load CSV files into DataFrames
    departments_df = pd.read_csv(base_path / "departments.csv")
    employees_df = pd.read_csv(base_path / "employees.csv")
    merchants_df = pd.read_csv(base_path / "merchants.csv")
    expenses_df = pd.read_csv(base_path / "expenses.csv")
    compliance_rules_df = pd.read_csv(base_path / "compliance_rules.csv")

    # Create SQLite database and write tables
    db_path = base_path / "compliance_data.db"
    with sqlite3.connect(db_path) as conn:
        departments_df.to_sql("departments", conn, if_exists="replace", index=False)
        employees_df.to_sql("employees", conn, if_exists="replace", index=False)
        merchants_df.to_sql("merchants", conn, if_exists="replace", index=False)
        expenses_df.to_sql("expenses", conn, if_exists="replace", index=False)
        compliance_rules_df.to_sql("compliance_rules", conn, if_exists="replace", index=False)


if __name__ == "__main__":
    main()

