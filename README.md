\# Corporate Compliance Analytics Project



\### Diligent Assessment Submission



\## 1. Project Overview



This project simulates a real-world Governance, Risk, and Compliance (GRC) scenario. It uses an AI-assisted IDE (Cursor) to build an end-to-end data pipeline that:

1\.  \*\*Generates\*\* five interconnected, synthetic datasets representing corporate employee expenses.

2\.  \*\*Ingests\*\* this data from CSV files into a structured SQLite database.

3\.  \*\*Analyzes\*\* the data using a complex SQL query to automatically flag transactions that are non-compliant with company policy or involve high-risk vendors.



The entire process showcases the ability to use modern tools to rapidly prototype and develop data-driven solutions relevant to Diligent's core business.



\## 2. Step-by-Step Development Process



This project was built iteratively using a series of prompts.



\### Step 2.1: Generating Synthetic Data



\*\*Objective:\*\* To create a rich, realistic, and normalized dataset that could support a meaningful compliance analysis.



\*\*Logic:\*\* Rather than a simple, flat file, the data was structured across five normalized tables. This approach demonstrates an understanding of database design and allows for more complex, multi-join queries. A `merchant\_risk\_level` was included to add a GRC-specific dimension to the analysis.



\*\*Prompt given to Cursor IDE:\*\*

"Generate five interconnected synthetic datasets in CSV format for a corporate expense compliance system. Please ensure some expenses intentionally violate the compliance rules.

departments.csv: department\_id, department\_name, cost\_center\_code

employees.csv: employee\_id, full\_name, department\_id, job\_title

merchants.csv: merchant\_id, merchant\_name, merchant\_risk\_level

expenses.csv: expense\_id, employee\_id, merchant\_id, submission\_date, category, amount

compliance\_rules.csv: rule\_id, category, max\_amount, description

Generate at least 150 rows for expenses.csv..."

code

Code

\*\*Outcome:\*\* The AI successfully generated the five CSV files (`departments.csv`, `employees.csv`, `merchants.csv`, `expenses.csv`, `compliance\_rules.csv`), which formed the foundation of the project.



\*(This step was committed with `feat: Add synthetic corporate compliance data (5 CSVs)`)\*



---



\### Step 2.2: Ingesting Data into SQLite



\*\*Objective:\*\* To load the raw data from the CSV files into a persistent, queryable SQL database.



\*\*Logic:\*\* A Python script using the robust and standard libraries `pandas` (for efficient data handling) and `sqlite3` (for database interaction) was the ideal choice. This automates the data loading process and makes it repeatable.



\*\*Prompt given to Cursor IDE:\*\*

"Write a Python script named ingest\_data.py. The script must perform the following actions:

Import the pandas and sqlite3 libraries.

Read the five CSV files into five separate pandas DataFrames.

Establish a connection to a new SQLite database file named compliance\_data.db.

Write each DataFrame to a corresponding table in the database."

code

Code

\*\*Outcome:\*\* The AI generated the `ingest\_data.py` script. Running this script (`python ingest\_data.py`) successfully created the `compliance\_data.db` file populated with our data.



\*(This step was committed with `feat: Create script to ingest CSV data into SQLite DB`)\*



---



\### Step 2.3: Analyzing for Compliance Violations



\*\*Objective:\*\* The core of the project. To query the database to identify and report on all suspicious transactions.



\*\*Logic:\*\* A sophisticated SQL query involving multiple `JOIN`s was required to bring all the relational data together. The query filters using `OR` logic to find transactions that breach the rules in two ways: (1) exceeding the `max\_amount` for its category, or (2) occurring at a merchant designated as 'High' risk. This demonstrates a practical application of SQL for business intelligence and risk detection.



\*\*Prompt given to Cursor IDE:\*\*

"Write a sophisticated SQL query to run against the compliance\_data.db database that identifies high-risk and non-compliant employee expenses.

The query must join all five tables to link employees, departments, merchants, and rules to each expense.

The query should filter for transactions that meet EITHER of these two conditions:

The expense amount is greater than the max\_amount for its category.

The merchant\_risk\_level is 'High'.

Also, provide the full Python script... to execute this query and print the results as a clean, formatted table."

code

Code

\*\*Outcome:\*\* The AI generated the `analyze\_expenses.py` script. Running this script (`python analyze\_expenses.py`) connects to the database, executes the complex query, and prints a final, clear report of all flagged expenses.



\*(This step was committed with `feat: Implement expense analysis to flag violations`)\*



\## 3. How to Run This Project



1\.  \*\*Prerequisites:\*\* Ensure you have Python and `pandas` installed (`pip install pandas`).

2\.  \*\*Populate Database:\*\* From your terminal, run the ingestion script:

&nbsp;   ```bash

&nbsp;   python ingest\_data.py

&nbsp;   ```

3\.  \*\*Run Analysis:\*\* Execute the analysis script to see the final report of non-compliant expenses:

&nbsp;   ```bash

&nbsp;   python analyze\_expenses.py

&nbsp;   ```

