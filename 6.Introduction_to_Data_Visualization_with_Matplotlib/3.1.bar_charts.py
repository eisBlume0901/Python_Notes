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