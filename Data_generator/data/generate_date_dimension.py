import pandas as pd

from config import START_DATE, END_DATE


def generate_date_dimension():

    dates = pd.date_range(
        START_DATE,
        END_DATE,
        freq="D"
    )

    data = []

    for date in dates:

        data.append({

            "date_id": int(
                date.strftime("%Y%m%d")
            ),

            "full_date": date.date(),

            "day_number": date.day,

            "day_name": date.strftime("%A"),

            "week_number": int(
                date.isocalendar().week
            ),

            "month_number": date.month,

            "month_name": date.strftime("%B"),

            "quarter_number":
                date.quarter,

            "quarter_name":
                f"Q{date.quarter}",

            "year_number":
                date.year,

            "is_weekend":
                date.weekday() >= 5
        })

    return pd.DataFrame(data)


if __name__ == "__main__":

    df = generate_date_dimension()

    print(df.head())

    print("\nTotal dates:")
    print(len(df))

    print("\nYears:")
    print(
        df["year_number"].unique()
    )