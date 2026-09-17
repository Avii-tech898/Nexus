import os
import pandas as pd


DATA_FOLDER = "../data"


def load_data(filename):

    path = os.path.join(
        DATA_FOLDER,
        filename
    )

    return pd.read_csv(path)


def check_duplicates(df, column):

    return df[column].duplicated().sum()


def check_missing(df):

    return df.isnull().sum().sum()


def main():

    print("\n")
    print("=" * 65)
    print("           NEXUS DATA QUALITY ENGINE")
    print("=" * 65)


    # -----------------------------
    # LOAD DATA
    # -----------------------------

    stores = load_data("stores.csv")
    employees = load_data("employees.csv")
    customers = load_data("customers.csv")
    products = load_data("products.csv")
    orders = load_data("orders.csv")
    order_items = load_data("order_items.csv")
    inventory = load_data("inventory.csv")
    returns = load_data("returns.csv")
    dates = load_data("date_dimension.csv")


    print("\nDATASET ROW COUNTS")

    print("Stores:", len(stores))
    print("Employees:", len(employees))
    print("Customers:", len(customers))
    print("Products:", len(products))
    print("Orders:", len(orders))
    print("Order Items:", len(order_items))
    print("Inventory:", len(inventory))
    print("Returns:", len(returns))
    print("Dates:", len(dates))


    # -----------------------------
    # DUPLICATE CHECK
    # -----------------------------

    print("\nDUPLICATE PRIMARY KEYS")

    print(
        "Stores:",
        check_duplicates(
            stores,
            "store_id"
        )
    )

    print(
        "Employees:",
        check_duplicates(
            employees,
            "employee_id"
        )
    )

    print(
        "Customers:",
        check_duplicates(
            customers,
            "customer_id"
        )
    )

    print(
        "Products:",
        check_duplicates(
            products,
            "product_id"
        )
    )

    print(
        "Orders:",
        check_duplicates(
            orders,
            "order_id"
        )
    )

    print(
        "Order Items:",
        check_duplicates(
            order_items,
            "order_item_id"
        )
    )


    # -----------------------------
    # MISSING VALUES
    # -----------------------------

    print("\nMISSING VALUES")

    datasets = {
        "Stores": stores,
        "Employees": employees,
        "Customers": customers,
        "Products": products,
        "Orders": orders,
        "Order Items": order_items,
        "Inventory": inventory,
        "Returns": returns,
        "Dates": dates
    }

    for name, df in datasets.items():

        missing = check_missing(df)

        print(
            f"{name}: {missing}"
        )


    # -----------------------------
    # FOREIGN KEY CHECKS
    # -----------------------------

    print("\nFOREIGN KEY VALIDATION")


    invalid_customer_ids = (
        ~orders["customer_id"]
        .isin(customers["customer_id"])
    ).sum()

    print(
        "Invalid Customer IDs:",
        invalid_customer_ids
    )


    invalid_product_ids = (
        ~order_items["product_id"]
        .isin(products["product_id"])
    ).sum()

    print(
        "Invalid Product IDs:",
        invalid_product_ids
    )


    invalid_order_ids = (
        ~order_items["order_id"]
        .isin(orders["order_id"])
    ).sum()

    print(
        "Invalid Order IDs:",
        invalid_order_ids
    )


    invalid_store_ids = (
        inventory["store_id"]
        .isin(stores["store_id"])
        == False
    ).sum()

    print(
        "Invalid Inventory Store IDs:",
        invalid_store_ids
    )


    # -----------------------------
    # NEGATIVE VALUE CHECK
    # -----------------------------

    print("\nNEGATIVE VALUE CHECK")


    negative_prices = (
        products["selling_price"] < 0
    ).sum()

    negative_costs = (
        products["unit_cost"] < 0
    ).sum()

    negative_revenue = (
        orders["total_amount"] < 0
    ).sum()

    negative_refunds = (
        returns["refund_amount"] < 0
    ).sum()


    print(
        "Negative Product Prices:",
        negative_prices
    )

    print(
        "Negative Product Costs:",
        negative_costs
    )

    print(
        "Negative Order Revenue:",
        negative_revenue
    )

    print(
        "Negative Refunds:",
        negative_refunds
    )


    # -----------------------------
    # REVENUE RECONCILIATION
    # -----------------------------

    print("\nREVENUE RECONCILIATION")


    item_revenue = (
        order_items["total_price"]
        .sum()
    )

    order_revenue = (
        orders["total_amount"]
        .sum()
    )


    difference = round(
        item_revenue - order_revenue,
        2
    )


    print(
        "Order Items Revenue:",
        f"₹{item_revenue:,.2f}"
    )

    print(
        "Orders Revenue:",
        f"₹{order_revenue:,.2f}"
    )

    print(
        "Difference:",
        f"₹{difference:,.2f}"
    )


    # -----------------------------
    # FINAL RESULT
    # -----------------------------

    print("\n")
    print("=" * 65)

    if difference == 0:

        print(
            "✅ REVENUE RECONCILIATION PASSED"
        )

    else:

        print(
            "❌ REVENUE RECONCILIATION FAILED"
        )


    print("=" * 65)


if __name__ == "__main__":

    main()
    