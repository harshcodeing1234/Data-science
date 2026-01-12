import pandas as pd #type:ignore
import matplotlib.pyplot as plt #type:ignore

data = {
    'Product':['Laptop','Mobile','Tablet','Headphones'],
    'Sales':[50000,70000,30000,20000]
}
# Save Dataset
df =pd.DataFrame(data)
df.to_csv('product_sales.csv')

# Vertical bar chart
plt.barh(df['Product'],df['Sales'],color='yellow')
plt.show()

# Horizontal bar chart
plt.barh(df['Product'],df['Sales'],color='yellow')
plt.show()

# Pie chart with percentages
plt.pie(df['Sales'],labels=df['Product'],autopct='%1.1f%%')
plt.title('Pie chart of Sales over product')
plt.show()

# Histogram of sales values 
plt.hist(df['Sales'],bins=5,color='orange',edgecolor='black')
plt.title('Histogram of sales')
plt.show()

'_______________________________________________________________________________________________________________'