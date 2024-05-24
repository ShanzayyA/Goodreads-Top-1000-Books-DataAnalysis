import pandas as pd

# Make sure these packages are installed:
# pandas, openpyxl

# Load the CSV file into a pandas DataFrame
books = pd.read_csv('/path/to/good_reads_top_1000_books.csv')

# Explore the data
print(books.info())
print(books.shape)

# Assuming 'author' and 'year' columns exist and are correctly named
print(books['author'].value_counts())  # Count books per author
print(books['year'].value_counts())    # Count books per year

# Data manipulation examples
# Normalize ratings to a scale of 0 to 1 (if applicable)
if 'rating' in books.columns:
    books['normalized_ratings'] = books['rating'] / books['rating'].max()

# Categorize books based on normalized ratings (if applicable)
if 'normalized_ratings' in books.columns:
    books['rating_category'] = books['normalized_ratings'].apply(
        lambda x: 'High' if x > 0.8 else ('Medium' if x > 0.5 else 'Low'))

# Save the manipulated data to a new Excel file
books.to_excel('/path/to/good_reads_final.xlsx', sheet_name='Data')

# Print the first few rows to review changes
print(books.head())
