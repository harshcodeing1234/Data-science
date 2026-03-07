### Exploratory Data Analysis (EDA) Steps:
___
1. Examine the dataset to know the number of rows, columns, and data types.

2. Use histograms to visualize how numeric data is distributed. `df.hist(bins=10 figsize=(20,15))` 

3. Box plots help identify outliers and show the five-number summary (min, Q1, median, Q3, max).

        `df.plot(kind='box', subplots=True, layout=(4,4), figsize=(12,10))`

4. For categorical variables, use bar charts or countplots to see category frequencies. `plt.bar() or sns.countplot()`

5. Use a correlation heatmap to identify relationships between variables.`sns.heatmap(df.corr())`

6. Use a scatter plot to identify linear or non-linear relationships.`plt.scatter()`

7. use pie chart when showing the percentage distribution of categories.. like `fire,not fire`

8. create a bar plot When features represent time (month, day, year), use bar charts to analyze trends.


