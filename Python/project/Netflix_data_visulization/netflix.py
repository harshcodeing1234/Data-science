# import module
import pandas as pd #type: ignore
import matplotlib.pyplot as plt #type: ignore

# load data
df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())
# clean data
df= df.dropna(subset=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'listed_in', 'description'])

# create bar charts for see movie vs tv shows
type_count = df['type'].value_counts()
plt.bar(type_count.index, type_count.values, color=['orange','blue'])
plt.title("Number of Movies and Tv shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Counts")
plt.savefig("shows_bar.png")
plt.show()

# content ratings
rating_count = df['rating'].value_counts()
plt.pie(rating_count, labels=rating_count.index, autopct='%1.1f%%')
plt.title("percentage of Content Ratings")
plt.savefig("ratings_pie.png")
plt.show()

# movie duration
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)
plt.hist(movie_df['duration_int'], bins=30, color='blue',edgecolor='black')
plt.title("Distribution of movie duration")
plt.xlabel("Duration in minutes")
plt.ylabel("No. of movies")
plt.savefig("duration_hist.png")
plt.show()

# Release year vs no. of shows
release_count = df['release_year'].value_counts()
plt.scatter(release_count.index, release_count.values, color='orange')
plt.title("Release year vs no. of movies")
plt.xlabel("Release Year")
plt.ylabel("No. of movies")
plt.savefig("release_year_scatter.png")
plt.show()


# bar charts to show country release
country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='orange')
plt.grid()
plt.title("Top 10 County release movies and shows")
plt.xlabel("Total no. of movies")
plt.ylabel("Country")
plt.savefig('country release_barh.png')
plt.show()

# Comaprision movie vs Tv shows
fig, ax = plt.subplots(1, 2, figsize=(10,5))

# Movies by year
movie_year_count = movie_df['release_year'].value_counts().sort_index()
ax[0].plot(movie_year_count.index, movie_year_count.values, color='orange')
ax[0].set_title("Movies by Release Year")

# TV Shows by year
tv_df = df[df['type'] == 'TV Show'].copy()
tv_year_count = tv_df['release_year'].value_counts().sort_index()
ax[1].plot(tv_year_count.index, tv_year_count.values, color='blue')
ax[1].set_title("TV Shows by Release Year")

plt.tight_layout()
plt.savefig('movie_tv shows.plot.png')
plt.show()
