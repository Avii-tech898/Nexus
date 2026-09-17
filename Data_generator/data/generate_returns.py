import random
import pandas as pd

from config import RANDOM_SEED


random.seed(RANDOM_SEED)


RETURN_REASONS = [
    "Damaged Product",
    "Wrong Product",
    "Product Not as Expected",
    "Quality Issue",
    "Size/Fit Issue",
    "Late Delivery",
    "Changed Mind"
]


def generate_returns(order_items, orders):

    returns = []

    return_id = 1

    # Approximately 6% of order items become returns
    for _, item in order_items.iterrows():

        if random.random() > 0.06:
            continue

        order_id = int(item["order_id"])

        order = orders[
            orders["order_id"] == order_id
        ].iloc[0]

        quantity = int(item["quantity"])

        return_quantity = random.randint(
            1,
            quantity
        )

        unit_price = float(
            item["unit_price"]
        )

        refund_amount = round(
            return_quantity * unit_price,
            2
        )

        returns.append({

            "return_id": return_id,

            "order_id": order_id,

            "order_item_id":
                int(item["order_item_id"]),

            "customer_id":
                int(order["customer_id"]),

            "product_id":
                int(item["product_id"]),

            "return_date":
                order["order_date"],

            "return_quantity":
                return_quantity,

            "return_reason":
                random.choice(RETURN_REASONS),

            "refund_amount":
                refund_amount,

            "return_status":
                "Completed"
        })

        return_id += 1

    return pd.DataFrame(returns)


if __name__ == "__main__":

    print(
        "This module expects "
        "orders and order_items DataFrames."
    )