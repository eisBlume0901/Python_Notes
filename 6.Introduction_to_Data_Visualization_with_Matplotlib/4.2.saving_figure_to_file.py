import matplotlib.pyplot as plt

mushroom_village_icecream_flavor_sales = {
    "Strawberry": 25,
    "Mint Chocolate": 50,
    "Mango": 45,
    "Vanilla": 30,
    "Chocolate Chip": 10
}

flavors = list(mushroom_village_icecream_flavor_sales.keys())
sales = list(mushroom_village_icecream_flavor_sales.values())

figure, axis = plt.subplots()
figure.set_size_inches([7, 4]) # width=7, length=3
axis.bar(flavors, sales)
axis.set_xlabel("Flavors")
axis.set_ylabel("Sales")
axis.set_xticks(range(len(flavors)))
axis.set_xticklabels(flavors, rotation=45)
plt.tight_layout()
plt.show()

# Saving plots as files (png, svg, jpeg)
figure.savefig("mushroom_village_icecream_sales.png")
figure.savefig("mushroom_village_icecream_sales_in_jpeg.jpg", dpi=300) # dpi = dots per inch

# dpi standards
# use 72-150 - web and online content
# use 150-300 - good for standard print quality (documentations and presentations)
# use 300-600 - high quality prints (professional photos and detailed graphics)
# use 600+ - extremely detailed prints or large format printing

# jpg vs png
# jpg - lossy compression, resulting in smaller file sizes but potential quality loss
# (best for photographs and website - reduce bandwidth usage and improve page load times)
# png - use lossless compression, preserving image quality and supporting transparency; ideal
# for images with text, sharp lines, or transparency needs