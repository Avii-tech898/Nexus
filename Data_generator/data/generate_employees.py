import random
import pandas as pd

from config import NUM_EMPLOYEES, NUM_STORES, RANDOM_SEED


random.seed(RANDOM_SEED)


FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Karan", "Vikram", "Ananya", "Priya",
    "Sneha", "Neha", "Pooja", "Kavya", "Isha",
    "Aditi", "Simran", "Riya", "Meera", "Nisha"
]

LAST_NAMES = [
    "Sharma", "Verma", "Singh", "Gupta", "Tripathi",
    "Yadav", "Mishra", "Patel", "Khan", "Das",
    "Jain", "Malhotra", "Agarwal", "Tiwari"
]

JOB_ROLES = [
    "Sales Executive",
    "Sales Manager",
    "Store Associate",
    "Store Manager",
    "Operations Executive",
    "Inventory Manager"
]

DEPARTMENTS = [
    "Sales",
    "Operations",
    "Inventory"
]


def generate_employees():

    employees = []

    for employee_id in range(1, NUM_EMPLOYEES + 1):

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        job_role = random.choice(JOB_ROLES)

        if "Sales" in job_role:
            department = "Sales"
        elif "Inventory" in job_role:
            department = "Inventory"
        else:
            department = random.choice(DEPARTMENTS)

        employee = {
            "employee_id": employee_id,
            "first_name": first_name,
            "last_name": last_name,
            "job_role": job_role,
            "department": department,
            "store_id": random.randint(1, NUM_STORES),
            "hire_date": pd.Timestamp(
                random.choice(
                    pd.date_range(
                        "2018-01-01",
                        "2024-12-31"
                    )
                )
            ).date(),
            "salary": round(
                random.uniform(18000, 85000),
                2
            ),
            "employment_status": random.choices(
                ["Active", "Inactive"],
                weights=[95, 5],
                k=1
            )[0]
        }

        employees.append(employee)

    return pd.DataFrame(employees)


if __name__ == "__main__":

    df = generate_employees()

    print(df.head())
    print("\nTotal employees:", len(df))
    print("\nDepartments:")
    print(df["department"].value_counts())