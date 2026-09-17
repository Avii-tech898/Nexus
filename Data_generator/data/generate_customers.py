import random
import pandas as pd

from config import NUM_CUSTOMERS, RANDOM_SEED


random.seed(RANDOM_SEED)


FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
    "Rohan", "Karan", "Vikram", "Ananya", "Priya",
    "Sneha", "Neha", "Pooja", "Kavya", "Isha",
    "Aditi", "Simran", "Riya", "Meera", "Nisha",
    "Ayush", "Dev", "Ravi", "Sakshi", "Shreya"
]

LAST_NAMES = [
    "Sharma", "Verma", "Singh", "Gupta", "Tripathi",
    "Yadav", "Mishra", "Patel", "Khan", "Das",
    "Jain", "Malhotra", "Agarwal", "Tiwari", "Pandey"
]

CITY_DATA = {
    "Delhi": "Delhi",
    "Lucknow": "Uttar Pradesh",
    "Jaipur": "Rajasthan",
    "Chandigarh": "Chandigarh",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Surat": "Gujarat",
    "Bengaluru": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Hyderabad": "Telangana",
    "Kochi": "Kerala",
    "Kolkata": "West Bengal",
    "Bhubaneswar": "Odisha",
    "Patna": "Bihar",
    "Guwahati": "Assam",
    "Bhopal": "Madhya Pradesh",
    "Indore": "Madhya Pradesh",
    "Nagpur": "Maharashtra",
    "Raipur": "Chhattisgarh"
}


def generate_customers():

    customers = []

    cities = list(CITY_DATA.keys())

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        city = random.choice(cities)
        state = CITY_DATA[city]

        gender = random.choice([
            "Male",
            "Female"
        ])

        birth_date = pd.Timestamp(
            random.choice(
                pd.date_range(
                    "1970-01-01",
                    "2005-12-31"
                )
            )
        ).date()

        registration_date = pd.Timestamp(
            random.choice(
                pd.date_range(
                    "2022-01-01",
                    "2025-12-31"
                )
            )
        ).date()

        customer = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "date_of_birth": birth_date,
            "email": f"customer{customer_id}@nexusretail.com",
            "phone": f"9{random.randint(100000000, 999999999)}",
            "city": city,
            "state": state,
            "country": "India",
            "registration_date": registration_date,
            "customer_segment": random.choice([
                "New",
                "Regular",
                "Premium"
            ])
        }

        customers.append(customer)

    return pd.DataFrame(customers)


if __name__ == "__main__":

    df = generate_customers()

    print(df.head())

    print("\nTotal customers:", len(df))

    print("\nCustomer segments:")
    print(df["customer_segment"].value_counts())

    print("\nTop cities:")
    print(df["city"].value_counts().head(10))