import random
import pandas as pd

from config import (
    NUM_STORES,
    RANDOM_SEED
)


random.seed(RANDOM_SEED)


def generate_inventory(products):

    inventory = []

    inventory_id = 1

    for store_id in range(1, NUM_STORES + 1):

        # Select products available in this store
        for _, product in products.iterrows():

            stock_quantity = random.randint(
                0,
                500
            )

            reorder_level = random.randint(
                20,
                100
            )

            reorder_quantity = random.randint(
                50,
                300
            )

            last_restock_date = pd.Timestamp(
                random.choice(
                    pd.date_range(
                        "2025-01-01",
                        "2025-12-31"
                    )
                )
            ).date()

            next_restock_date = (
                pd.Timestamp(
                    last_restock_date
                ) + pd.Timedelta(
                    days=random.randint(7, 45)
                )
            ).date()

            if stock_quantity == 0:

                inventory_status = "Out of Stock"

            elif stock_quantity <= reorder_level:

                inventory_status = "Low Stock"

            elif stock_quantity >= 400:

                inventory_status = "Overstock"

            else:

                inventory_status = "In Stock"

            inventory.append({

                "inventory_id": inventory_id,

                "product_id": int(
                    product["product_id"]
                ),

                "store_id": store_id,

                "stock_quantity": stock_quantity,

                "reorder_level": reorder_level,

                "reorder_quantity": reorder_quantity,

                "last_restock_date":
                    last_restock_date,

                "next_restock_date":
                    next_restock_date,

                "inventory_status":
                    inventory_status
            })

            inventory_id += 1

    return pd.DataFrame(inventory)


if __name__ == "__main__":

    print(
        "This module expects a "
        "products DataFrame."
    )