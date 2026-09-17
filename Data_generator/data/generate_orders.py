import random
import pandas as pd

from config import (
    NUM_ORDERS,
    NUM_CUSTOMERS,
    NUM_STORES,
    NUM_EMPLOYEES,
    START_DATE,
    END_DATE,
    PAYMENT_METHODS,
    ORDER_STATUSES,
    CHANNELS,
    RANDOM_SEED
)


random.seed(RANDOM_SEED)


def generate_orders(customers=None):

    orders = []
    customer_locations = {}

    if customers is not None:
        customer_locations = (
            customers
            .set_index("customer_id")[["city", "state"]]
            .to_dict("index")
        )

    date_range = pd.date_range(
        START_DATE,
        END_DATE
    )

    for order_id in range(1, NUM_ORDERS + 1):

        order_date = random.choice(date_range).date()

        channel = random.choice(CHANNELS)

        # Online orders don't need a physical store
        if channel == "Online":
            store_id = None
        else:
            store_id = random.randint(
                1,
                NUM_STORES
            )

        employee_id = random.randint(
            1,
            NUM_EMPLOYEES
        )

        customer_id = random.randint(
            1,
            NUM_CUSTOMERS
        )

        customer_location = customer_locations.get(
            customer_id,
            {}
        )

        shipping_city = customer_location.get("city")
        shipping_state = customer_location.get("state")
    

        payment_method = random.choice(
            PAYMENT_METHODS
        )

        order_status = random.choice(
            ORDER_STATUSES
        )

        # Temporary values.
        # Final revenue will come from order_items.
        total_amount = round(
            random.uniform(300, 50000),
            2
        )

        discount_amount = round(
            total_amount *
            random.uniform(0, 0.15),
            2
        )

        shipping_cost = round(
            random.uniform(0, 500),
            2
        )

        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "store_id": store_id,
            "employee_id": employee_id,
            "order_date": order_date,
            "order_status": order_status,
            "channel": channel,
            "payment_method": payment_method,
            "shipping_city": shipping_city,
            "shipping_state": shipping_state,
            "shipping_country": "India",
            "total_amount": total_amount,
            "discount_amount": discount_amount,
            "shipping_cost": shipping_cost
        }

        orders.append(order)

    return pd.DataFrame(orders)


if __name__ == "__main__":

    df = generate_orders()

    print(df.head())

    print("\nTotal orders:", len(df))

    print("\nChannel distribution:")
    print(df["channel"].value_counts())

    print("\nOrder status:")
    print(df["order_status"].value_counts())

    print("\nPayment methods:")
    print(df["payment_method"].value_counts())

    print("\nOnline orders:",
          df["channel"].eq("Online").sum())

    print("Store orders:",
          df["channel"].eq("Store").sum())