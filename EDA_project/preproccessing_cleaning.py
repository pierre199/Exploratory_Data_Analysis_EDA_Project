import pandas as pd

# Read the data from the original CSV file
data = pd.read_csv("googlestore.csv")

# Remove the "price" column
data_cleaned_1 = data.drop("Price", axis=1)

# Count the initial number of records
initial_records = len(data_cleaned_1)

# Remove rows with errors or incomplete cells
data_cleaned_2 = data_cleaned_1.dropna()

# Count the final number of records
final_records = len(data_cleaned_2)

# Calculate the number of removed records
removed_records = initial_records - final_records

# Extract secondary genres from the "Genres" column
data_cleaned_2.insert(data.columns.get_loc("Genres") + 0, "secondary Genres", data_cleaned_2["Genres"].str.split(";", expand=True)[1])

# Remove semicolon and text after it from the "Genres" column
data_cleaned_2["Genres"] = data_cleaned_2["Genres"].str.split(";", n=1).str[0]

# Convert "Type" column to uppercase
data_cleaned_2["Type"] = data_cleaned_2["Type"].str.upper()

# Convert the date column to datetime format
data_cleaned_2['Last Updated'] = pd.to_datetime(data_cleaned_2['Last Updated'], format='%d-%m-%Y')

# Extract year, month, and day components
data_cleaned_2['Year'] = data_cleaned_2['Last Updated'].dt.year
data_cleaned_2['Month'] = data_cleaned_2['Last Updated'].dt.month
data_cleaned_2['Day'] = data_cleaned_2['Last Updated'].dt.day



# Write the modified data to a new CSV file
data_cleaned_2.to_csv("googlestore_cleaned.csv", index=False)

print("Clean data has been saved to 'googlestore_Clean.csv'.")
