# NEXUS Data Generator Configuration
import os
DATA_FOLDER = "../data"

# =============================
# DATASET SIZE
# =============================

NUM_CUSTOMERS = 10_000
NUM_PRODUCTS = 1_000
NUM_STORES = 20
NUM_EMPLOYEES = 100
NUM_ORDERS = 50_000

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5


# =============================
# DATE RANGE
# =============================

START_DATE = "2023-01-01"
END_DATE = "2025-12-31"


# =============================
# BUSINESS CONFIGURATION
# =============================

COUNTRY = "India"

REGIONS = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

PRODUCT_CATEGORIES = [
    "Electronics",
    "Home Appliances",
    "Fashion",
    "Beauty",
    "Grocery",
    "Sports"
]


# =============================
# ORDER CONFIGURATION
# =============================

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

ORDER_STATUSES = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Cancelled"
]

CHANNELS = [
    "Online",
    "Online",
    "Online",
    "Store"
]


# =============================
# OUTPUT CONFIGURATION
# =============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(
    BASE_DIR,
    "data"
)

RANDOM_SEED = 42