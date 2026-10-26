schema = """
Table: Students

Columns:
student_id INTEGER
name VARCHAR(50)
department VARCHAR(50)
marks INTEGER
"""

requirement = """
Display the names and marks of students who scored
more than 80 marks, ordered by marks in descending order.
"""

prompt = f"""
Role: SQL query assistant

Database schema:
{schema}

Requirement:
{requirement}

Generate one valid SQL SELECT query.
Use only the listed table and columns.
"""

generated_sql = """
SELECT name, marks
FROM Students
WHERE marks > 80
ORDER BY marks DESC;
"""

print("Structured Prompt:")
print(prompt)

print("Generated SQL Query:")
print(generated_sql)