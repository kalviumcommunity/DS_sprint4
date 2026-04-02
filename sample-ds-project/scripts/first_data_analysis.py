"""
Simple standalone Python script for basic data analysis.

This script uses a small in-memory sales dataset, performs a few
calculations, and prints the results to the console.
"""


def analyze_weekly_sales():
    """Calculate and print summary statistics for a simple sales list."""
    daily_sales = [120, 135, 150, 128, 160, 145, 155]
    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    total_sales = sum(daily_sales)
    average_sales = total_sales / len(daily_sales)
    highest_sales = max(daily_sales)
    lowest_sales = min(daily_sales)

    highest_day = day_names[daily_sales.index(highest_sales)]
    lowest_day = day_names[daily_sales.index(lowest_sales)]

    days_above_average = []
    for day, sales in zip(day_names, daily_sales):
        if sales > average_sales:
            days_above_average.append(day)

    print("Weekly Sales Analysis")
    print("-" * 24)
    print(f"Daily sales values: {daily_sales}")
    print(f"Total sales: {total_sales}")
    print(f"Average daily sales: {average_sales:.2f}")
    print(f"Highest sales: {highest_sales} on {highest_day}")
    print(f"Lowest sales: {lowest_sales} on {lowest_day}")
    print(f"Days above average: {', '.join(days_above_average)}")


if __name__ == "__main__":
    print("Starting the data analysis script...")
    analyze_weekly_sales()
    print("Script execution finished.")
