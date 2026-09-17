import random
import pandas as pd

from config import NUM_STORES, REGIONS, COUNTRY, RANDOM_SEED


random.seed(RANDOM_SEED)


cities_by_region = {
    "North": ["Delhi", "Lucknow", "Chandigarh", "Jaipur"],
    "South": ["Bengaluru", "Chennai", "Hyderabad", "Kochi"],
    "East": ["Kolkata", "Bhubaneswar", "Patna", "Guwahati"],
    "West": ["Mumbai", "Pune", "Ahmedabad", "Surat"],
    "Central": ["Bhopal", "Indore", "Nagpur", "Raipur"]
}


def generate_stores():

    stores = []

    for store_id in range(1, NUM_STORES + 1):

        region = random.choice(REGIONS)
        city = random.choice(cities_by_region[region])

        store = {
            "store_id": store_id,
            "store_name": f"NEXUS Store {store_id:03d}",
            "store_type": random.choice(
                ["Retail", "Retail", "Warehouse"]
            ),
            "city": city,
            "state": "India",
            "country": COUNTRY,
            "region": region,
            "opening_date": pd.Timestamp(
                random.choice(
                    pd.date_range(
                        "2018-01-01",
                        "2023-12-31"
                    )
                )
            ).date(),
            "store_status": "Active"
        }

        stores.append(store)

    return pd.DataFrame(stores)


if __name__ == "__main__":

    df = generate_stores()

    print(df.head())
    print("\nTotal stores:", len(df))