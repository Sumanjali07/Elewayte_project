import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("Housing.csv")

#Question 1:How many houses are in the range of prices from 0-25lakhs, 26-50lakhs, 51-75lakhs, 76-100lakhs and >100lakhs. Visualize it using a line chart also
bins = [0, 2500000, 5000000, 7500000, 10000000, float('inf')]
labels = ['0-25L', '26-50L', '51-75L', '76-100L', '>100L']
df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels)

price_counts = df['price_range'].value_counts().sort_index()

price_counts.plot(kind='line', marker='o', title='House Counts by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Number of Houses')
plt.grid(True)
plt.show()

#Question 2:Find average house prices for houses having AC and nonAC. Plot the relationship using a barchart.
avg_prices_ac = df.groupby('airconditioning')['price'].mean()

avg_prices_ac.plot(kind='bar', title='Average Price: AC vs Non-AC', color=['skyblue', 'orange'])
plt.xlabel('Air Conditioning')
plt.ylabel('Average Price')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

#Question 3:Simulate the relationship between parking and house price.
parking_price = df.groupby('parking')['price'].mean()

parking_price.plot(kind='line', marker='o', title='Parking vs Average Price')
plt.xlabel('Parking Spaces')
plt.ylabel('Average House Price')
plt.grid(True)
plt.show()

#Question 4:What is price gap between the houses having <5000sqft & no prefarea, and >5000sqft & there is prefarea?
group1 = df[(df['area'] < 5000) & (df['prefarea'] == 'no')]
group2 = df[(df['area'] > 5000) & (df['prefarea'] == 'yes')]

avg1 = group1['price'].mean()
avg2 = group2['price'].mean()
price_gap = abs(avg2 - avg1)

print(f"Average Price (Area <5000 & No Prefarea): ₹{avg1:.2f}")
print(f"Average Price (Area >5000 & Prefarea): ₹{avg2:.2f}")
print(f"Price Gap: ₹{price_gap:.2f}")