import random
import pandas as pd

from config import NUM_PRODUCTS, PRODUCT_CATEGORIES, RANDOM_SEED


random.seed(RANDOM_SEED)


BRANDS = [
    "NEXUS",
    "Samsung",
    "LG",
    "Sony",
    "Nike",
    "Adidas",
    "Puma",
    "Boat",
    "Philips",
    "HP",
    "Dell",
    "Lenovo",
    "Apple",
    "Whirlpool",
    "Prestige"
]


SUB_CATEGORIES = {
    "Electronics": [
        "Smartphones",
        "Laptops",
        "Headphones",
        "Smart Watches",
        "Accessories"
    ],

    "Home Appliances": [
        "Refrigerators",
        "Washing Machines",
        "Microwaves",
        "Air Conditioners",
        "Kitchen Appliances"
    ],

    "Fashion": [
        "Men Clothing",
        "Women Clothing",
        "Footwear",
        "Accessories"
    ],

    "Beauty": [
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrances"
    ],

    "Grocery": [
        "Snacks",
        "Beverages",
        "Packaged Food",
        "Household Essentials"
    ],

    "Sports": [
        "Fitness Equipment",
        "Sportswear",
        "Cricket",
        "Football",
        "Outdoor"
    ]
}


def generate_products():

    products = []

    for product_id in range(1, NUM_PRODUCTS + 1):

        category = random.choice(PRODUCT_CATEGORIES)

        sub_category = random.choice(
            SUB_CATEGORIES[category]
        )

        brand = random.choice(BRANDS)

        unit_cost = round(
            random.uniform(100, 50000),
            2
        )

        # Selling price is always higher than cost
        markup = random.uniform(1.10, 1.80)

        selling_price = round(
            unit_cost * markup,
            2
        )

        product = {
            "product_id": product_id,
            "product_name": (
                f"{brand} "
                f"{sub_category} "
                f"Model-{product_id:04d}"
            ),
            "category": category,
            "sub_category": sub_category,
            "brand": brand,
            "unit_cost": unit_cost,
            "selling_price": selling_price,
            "supplier_name": (
                f"Supplier-{random.randint(1, 50):03d}"
            ),
            "launch_date": pd.Timestamp(
                random.choice(
                    pd.date_range(
                        "2020-01-01",
                        "2025-12-31"
                    )
                )
            ).date(),
            "product_status": random.choices(
                ["Active", "Discontinued"],
                weights=[95, 5],
                k=1
            )[0]
        }

        products.append(product)

    return pd.DataFrame(products)


if __name__ == "__main__":

    df = generate_products()

    print(df.head())

    print("\nTotal products:", len(df))

    print("\nCategories:")
    print(df["category"].value_counts())

    print("\nAverage selling price:")
    print(round(df["selling_price"].mean(), 2))

    print("\nAverage profit per unit:")

    profit = (
        df["selling_price"]
        - df["unit_cost"]
    )

    print(round(profit.mean(), 2))