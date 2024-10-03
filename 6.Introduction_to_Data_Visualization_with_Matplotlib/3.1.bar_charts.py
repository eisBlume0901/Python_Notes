import pandas as pd
import matplotlib.pyplot as plt


sales_icecream = [
    {
        "Village": "Mushroom Village",
        "Strawberry": 25,
        "Vanilla": 10,
        "Pistachio": 5,
        "Mint Chocolate Chip": 15
    },
    {
        "Village": "Marine Village",
        "Strawberry": 10,
        "Vanilla": 5,
        "Pistachio": 30,
        "Mint Chocolate Chip": 20
    },
    {
        "Village": "Sky Village",
        "Strawberry": 17,
        "Vanilla": 12,
        "Pistachio": 15,
        "Mint Chocolate Chip": 25
    }
]

sales_icecream_df = pd.DataFrame(sales_icecream)
sales_icecream_df = sales_icecream_df.set_index("Village")
print(sales_icecream_df.head())

figure, axis = plt.subplots(figsize=(5, 10))

axis.bar(sales_icecream_df.index, sales_icecream_df["Strawberry"], label="Strawberry", color="pink")
axis.bar(sales_icecream_df.index, sales_icecream_df["Vanilla"], bottom=sales_icecream_df["Strawberry"], label="Vanilla", color="yellow")
axis.bar(sales_icecream_df.index, sales_icecream_df["Mint Chocolate Chip"], bottom=sales_icecream_df["Vanilla"] + sales_icecream_df["Strawberry"], label="Mint Chocolate Chip", color="green")
axis.bar(sales_icecream_df.index, sales_icecream_df["Pistachio"], bottom=sales_icecream_df["Mint Chocolate Chip"] + sales_icecream_df["Vanilla"] + sales_icecream_df["Strawberry"], label="Pistachio", color="brown")
# Set the positions of the x-ticks
axis.set_xticks(range(len(sales_icecream_df.index)))

# Set the labels for the x-ticks with rotation for better readability
axis.set_xticklabels(sales_icecream_df.index, rotation=35)
axis.set_ylabel("Number of Sales per piece")
axis.set_xlabel("Villages Name")
axis.set_title("Ice Cream Sales in Villages")
axis.legend()
plt.tight_layout()
plt.show()

data = {
    'date_time': ['2025-01-03 10:45:21', '2025-01-03 11:31:22', '2025-01-04 09:12:15', '2025-01-04 12:17:03', '2025-01-05 08:45:21', '2025-01-05 10:45:21', '2025-01-06 09:45:21'],
    'score': [21, 35, 41, 29, 28, 31, 32],
    'overall_score': [50, 50, 50, 30, 35, 40, 40]
}

data_df = pd.DataFrame(data)

data_df['percentage'] = (data_df['score'] / data_df['overall_score']) * 100

def set_color(percentage_series):
    colors = []
    for percentage in percentage_series:
        if percentage < 70:
            colors.append('#FEE140')
        else:
            colors.append('#DA384C')
    return colors

colors = set_color(data_df['percentage'])

figure1, axis1 = plt.subplots(figsize=(12, 7))
axis1.bar(data_df['date_time'], data_df['percentage'], color=colors)
axis1.set_xticks(range(len(data_df['date_time'])))
axis1.set_xticklabels(data_df['date_time'], rotation=35)
axis1.set_yticks(range(0, 101, 10))
axis1.set_ylabel("Score Percentage (%)")
axis1.set_xlabel("Date and Time")
plt.tight_layout()
plt.show()


