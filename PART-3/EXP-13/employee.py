employees = [
    {"name": "Ravi", "dept": "Sales", "salary": 30000},
    {"name": "Anita", "dept": "IT", "salary": 40000},
    {"name": "Kiran", "dept": "HR", "salary": 35000}
]

# 1. Update Sales salaries by 10%
for emp in employees:
    if emp["dept"] == "Sales":
        emp["salary"] *= 1.10
        
# 2. Update IT salaries by 5%
for emp in employees:
    if emp["dept"] == "IT":
        emp["salary"] *= 1.05
        
# 3. Update HR salaries by 8% and print
for emp in employees:
    if emp["dept"] =="HR":
        emp["salary"] *= 1.08
print(emp)
