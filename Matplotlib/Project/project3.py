import pandas as pd #type:ignore
import matplotlib.pyplot as plt #type:ignore

data = {
    'Day':[1,2,3,4,5,6,7],
    'Sales':[2000,2200,2100,2050,2189,2000,2500]
}
# Load & save Dataset
df =pd.DataFrame(data)
df.to_csv('Daily.sales.csv')


# Bar chart
plt.plot(df['Day'],df['Sales'],marker='o',linestyle='--',color='black',label='Sales over Day')
plt.legend()
plt.show()

# Highlight and annotate highest value
highest_value = df['Sales'].nlargest(5)
plt.plot(df['Day'],df['Sales'],marker='o',linestyle='--',color='black',label='Sales over Day')
for i in highest_value.index:
    plt.annotate(f'{df["Sales"][i]}', xy=(df['Day'][i], df['Sales'][i]), xytext=(df['Day'][i], df['Sales'][i]+50),
                 arrowprops=dict(facecolor='red', shrink=0.05))
plt.legend()
plt.show()

# Save plot as an image file
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')






