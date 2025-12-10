import sqlite3
import pandas as pd
from pathlib import Path

def main():
    db_path = Path(__file__).parent / "compliance_data.db"
    query = """
    SELECT
      e.full_name,
      d.department_name,
      x.submission_date,
      m.merchant_name,
      m.merchant_risk_level,
      x.amount,
      r.max_amount
    FROM expenses x
    JOIN employees e ON x.employee_id = e.employee_id
    JOIN departments d ON e.department_id = d.department_id
    JOIN merchants m ON x.merchant_id = m.merchant_id
    JOIN compliance_rules r ON x.category = r.category
    WHERE x.amount > r.max_amount
       OR m.merchant_risk_level = 'High'
    ORDER BY x.submission_date;
    """
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)

    # Nice, readable output
    if df.empty:
        print("No high-risk or non-compliant expenses found.")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()