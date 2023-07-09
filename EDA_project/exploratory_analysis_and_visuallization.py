import pandas as pd
import plotly.express as px


# Read the data from the original CSV file
data = pd.read_csv("googlestore.csv")

# Convert the "Rating" column to numeric and handle errors
data["Rating"] = pd.to_numeric(data["Rating"], errors="coerce")

# Remove rows with missing or invalid ratings
data = data.dropna(subset=["Rating"])
data = data[data["Rating"].between(0, 5)]

# Calculate the average rating for each category
average_ratings = data.groupby("Category")["Rating"].mean()

# Find the category with the highest average rating
highest_average_rating_category = average_ratings.idxmax()
highest_average_rating = average_ratings.max()

# Count the occurrences of each content rating
content_rating_counts = data["Content Rating"].value_counts()

# Find the most common content rating
most_common_rating = content_rating_counts.idxmax()

# Convert the "Rating" and "Reviews" columns to numeric
data["Rating"] = pd.to_numeric(data["Rating"], errors="coerce")
data["Reviews"] = pd.to_numeric(data["Reviews"], errors="coerce")

# Remove rows with missing or invalid ratings and reviews
data = data.dropna(subset=["Rating", "Reviews"])
data = data[data["Rating"].between(0, 5)]

# Create hover text with app names and data modification
hover_text = data["App"]
data["Installs"] = pd.to_numeric(data["Installs"].str.replace('[^\d.]', '', regex=True), errors='coerce')
content_rating = data['Content Rating']

# Create an interactive scatter plot that shows the relation between the no of reviews and rating using Plotly
nuofreviews_vs_rating = px.scatter(data, x="Reviews", y="Rating", hover_name=hover_text, size='Installs' ,color=content_rating , opacity=0.9, title="Number of Reviews vs App Rating")

# Remove non-numeric characters from the "Size" column
data["Size"] = data["Size"].str.replace("[^\d.]","", regex=True)

# Convert the "Size" column to numeric
data["Size"] = pd.to_numeric(data["Size"], errors="coerce")


# Create an interactive violin plot that show the relation between the app size and content rating using Plotly
appsize_VS_contentrating = px.violin(data, x="Content Rating", y="Size",  box=True, points="all",
                title="Distribution of App Size across Content Ratings",
                labels={"Content Rating": "Content Rating", "Size": "App Size (MB)"},
                hover_data={"App Name": data["App"]})

# Show the interactive plots
nuofreviews_vs_rating.show()
appsize_VS_contentrating.show()


# printing the resutls
print(f"The category with the highest average rating is '{highest_average_rating_category}' with an average rating of {highest_average_rating:.2f}.")

print(f"The most common content rating in the dataset is '{most_common_rating}'.")

