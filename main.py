import os
import pandas as pd

from config import DATA_FOLDER

from Data_generator.data.generate_stores import generate_stores
from Data_generator.data.generate_employees import generate_employees
from Data_generator.data.generate_customers import generate_customers
from Data_generator.data.generate_products import generate_products
from Data_generator.data.generate_orders import generate_orders
from Data_generator.data.generate_order_items import generate_order_items
from Data_generator.data.generate_inventory import generate_inventory
from Data_generator.data.generate_returns import generate_returns
from Data_generator.data.generate_date_dimension import generate_date_dimension


def save_csv(df, filename):

    os.makedirs(DATA_FOLDER, exist_ok=True)

    path = os.path.join(
        DATA_FOLDER,
        filename
    )

    df.to_csv(
        path,
        index=False
    )

    print(
        f"Saved: {filename} "
        f"({len(df):,} rows)"
    )


def main():

    print("\n")
    print("=" * 60)
    print("        NEXUS DATA GENERATION ENGINE")
    print("=" * 60)

    # --------------------------------
    # 1. MASTER DATA
    # --------------------------------

    print("\n[1/9] Generating stores...")

    stores = generate_stores()

    print(
        f"Stores: {len(stores):,}"
    )


    print("\n[2/9] Generating employees...")

    employees = generate_employees()

    print(
        f"Employees: {len(employees):,}"
    )


    print("\n[3/9] Generating customers...")

    customers = generate_customers()

    print(
        f"Customers: {len(customers):,}"
    )


    print("\n[4/9] Generating products...")

    products = generate_products()

    print(
        f"Products: {len(products):,}"
    )


    # --------------------------------
    # 2. TRANSACTION DATA
    # --------------------------------

    print("\n[5/9] Generating orders...")

    orders = generate_orders(customers)

    print(
        f"Orders: {len(orders):,}"
    )


    print("\n[6/9] Generating order items...")

    order_items = generate_order_items(
        orders,
        products
    )

    print(
        f"Order Items: {len(order_items):,}"
    )


    # --------------------------------
    # 3. REVENUE RECONCILIATION
    # --------------------------------

    print(
        "\n[Revenue] "
        "Calculating order totals..."
    )

    order_totals = (
        order_items
        .groupby("order_id")["total_price"]
        .sum()
        .reset_index()
    )

    order_totals.rename(
        columns={
            "total_price": "calculated_total"
        },
        inplace=True
    )


    orders = orders.drop(
        columns=[
            "total_amount",
            "discount_amount"
        ]
    )


    orders = orders.merge(
        order_totals,
        on="order_id",
        how="left"
    )


    orders.rename(
        columns={
            "calculated_total":
                "total_amount"
        },
        inplace=True
    )


    orders["total_amount"] = (
        orders["total_amount"]
        .fillna(0)
        .round(2)
    )


    # --------------------------------
    # 4. INVENTORY
    # --------------------------------

    print("\n[7/9] Generating inventory...")

    inventory = generate_inventory(
        products
    )

    print(
        f"Inventory: {len(inventory):,}"
    )


    # --------------------------------
    # 5. RETURNS
    # --------------------------------

    print("\n[8/9] Generating returns...")

    returns = generate_returns(
        order_items,
        orders
    )

    print(
        f"Returns: {len(returns):,}"
    )


    # --------------------------------
    # 6. DATE DIMENSION
    # --------------------------------

    print("\n[9/9] Generating date dimension...")

    date_dimension = (
        generate_date_dimension()
    )

    print(
        f"Dates: {len(date_dimension):,}"
    )


    # --------------------------------
    # 7. SAVE CSV FILES
    # --------------------------------

    print("\n")
    print("=" * 60)
    print("Saving CSV files...")
    print("=" * 60)

    save_csv(
        stores,
        "stores.csv"
    )

    save_csv(
        employees,
        "employees.csv"
    )

    save_csv(
        customers,
        "customers.csv"
    )

    save_csv(
        products,
        "products.csv"
    )

    save_csv(
        orders,
        "orders.csv"
    )

    save_csv(
        order_items,
        "order_items.csv"
    )

    save_csv(
        inventory,
        "inventory.csv"
    )

    save_csv(
        returns,
        "returns.csv"
    )

    save_csv(
        date_dimension,
        "date_dimension.csv"
    )


    # --------------------------------
    # 8. BASIC VALIDATION
    # --------------------------------

    print("\n")
    print("=" * 60)
    print("NEXUS DATA VALIDATION")
    print("=" * 60)

    print(
        "\nUnique Order IDs:",
        orders["order_id"].nunique()
    )

    print(
        "Unique Customer IDs:",
        customers["customer_id"].nunique()
    )

    print(
        "Unique Product IDs:",
        products["product_id"].nunique()
    )

    print(
        "Order Items Orders:",
        order_items["order_id"].nunique()
    )

    print(
        "Order Items Products:",
        order_items["product_id"].nunique()
    )

    print(
        "\nTotal Revenue:",
        f"₹{orders['total_amount'].sum():,.2f}"
    )

    print(
        "Total Refund:",
        f"₹{returns['refund_amount'].sum():,.2f}"
    )

    print("\n")
    print("=" * 60)
    print("       NEXUS DATA GENERATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":

    main()