import random
import pandas as pd

from config import (
    MIN_ITEMS_PER_ORDER,
    MAX_ITEMS_PER_ORDER,
    RANDOM_SEED
)


random.seed(RANDOM_SEED)


def generate_order_items(orders, products):

    order_items = []

    order_item_id = 1

    # Product popularity weights
    product_ids = products["product_id"].tolist()

    weights = []

    for _ in product_ids:

        popularity = random.random()

        if popularity < 0.10:
            weights.append(8)
        elif popularity < 0.35:
            weights.append(4)
        else:
            weights.append(1)

    for _, order in orders.iterrows():

        # Number of products in this order
        number_of_items = random.randint(
            MIN_ITEMS_PER_ORDER,
            MAX_ITEMS_PER_ORDER
        )

        selected_products = random.choices(
            product_ids,
            weights=weights,
            k=number_of_items
        )

        # Avoid duplicate product within same order
        selected_products = list(
            dict.fromkeys(selected_products)
        )

        for product_id in selected_products:

            product = products[
                products["product_id"] == product_id
            ].iloc[0]

            quantity = random.choices(
                [1, 2, 3, 4, 5],
                weights=[55, 25, 12, 6, 2],
                k=1
            )[0]

            unit_price = float(
                product["selling_price"]
            )

            # 0–15% discount
            discount_rate = random.uniform(
                0,
                0.15
            )

            gross_amount = (
                quantity * unit_price
            )

            discount_amount = round(
                gross_amount * discount_rate,
                2
            )

            total_price = round(
                gross_amount - discount_amount,
                2
            )

            order_item = {
                "order_item_id": order_item_id,
                "order_id": int(order["order_id"]),
                "product_id": int(product_id),
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_amount": discount_amount,
                "total_price": total_price
            }

            order_items.append(order_item)

            order_item_id += 1

    return pd.DataFrame(order_items)


if __name__ == "__main__":

    # Test mode
    print(
        "This module expects orders and products "
        "DataFrames."
    )