import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("netflix_titles.csv")

# Identify and handle missing values
# Display the count of missing values for each column
print("Missing values before handling:")
print(df.isnull().sum())

# For simplicity, let's fill numerical columns with their mean and categorical columns with their mode.
# More sophisticated methods could be used based on the nature of the missing data.

# Fill missing values in `director` and `cast` with 'Unknown' as they are categorical.
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

# Fill missing values in `country` with 'Unknown' as they are categorical.
df['country'] = df['country'].fillna('Unknown')

# Fill missing values in `date_added` with the mode as it is categorical.
df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])

# Fill missing values in `rating` with the mode as it is categorical.
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Display the count of missing values after handling
print("\nMissing values after handling:")
print(df.isnull().sum())

# Remove duplicate rows
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
rows_after_duplicates = df.shape[0]
print(f"\nRemoved {initial_rows - rows_after_duplicates} duplicate rows.")

# Standardize text values (gender, country names, etc.)
# For `country`, let's standardize by stripping whitespace and converting to title case.
df['country'] = df['country'].str.strip().str.title()
# For `type`, `listed_in`, and `rating`, we'll convert to title case and strip whitespace.
df['type'] = df['type'].str.strip().str.title()
df['listed_in'] = df['listed_in'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.title()


# Convert date formats to a consistent type (e.g., dd-mm-yyyy)
# Convert `date_added` to datetime objects
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# For demonstration, let's convert `release_year` to datetime objects as well.
# It is an integer, so we can convert it to datetime at the beginning of the year.
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')


# Rename column headers to be clean and uniform (e.g., lowercase, no spaces)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check and fix data types (e.g., age should be int, date as datetime)
# Display the data types after all operations
print("\nData types after cleaning:")
print(df.info())

# Save the cleaned data to a new CSV file
df.to_csv('netflix_titles_cleaned.csv', index=False)

print("\nData cleaning complete. Cleaned data saved to 'netflix_titles_cleaned.csv'")