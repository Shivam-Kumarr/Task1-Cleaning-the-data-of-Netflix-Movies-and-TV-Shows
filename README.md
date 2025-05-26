# Task1: Cleaning the Netflix Movies and TV Shows Dataset

This project focuses on cleaning and preparing the `netflix_titles.csv` dataset for analysis. The Python script performs several essential data cleaning operations to ensure data quality and consistency.

## What was done:

1.  **Missing Values Handled:** Filled missing values in `director`, `cast`, `country`, `date_added`, and `rating` columns.
2.  **Duplicate Rows Removed:** Ensured no duplicate entries exist in the dataset.
3.  **Text Standardization:** Standardized text fields (e.g., `country`, `type`, `rating`) to a consistent format (e.g., Title Case, stripped whitespace).
4.  **Date Format Conversion:** Converted `date_added` and `release_year` columns to proper datetime objects.
5.  **Column Renaming:** Renamed all column headers to lowercase with underscores (e.g., `date_added`).
6.  **Duration Column Refined:**
    * The `duration` column (which contained both minutes and seasons) was split.
    * Two new numerical columns, `duration_minutes` (for movies) and `num_seasons` (for TV shows), were created.
    * The original `duration` column was then removed.
7.  **Data Type Correction:** Ensured all columns have appropriate data types, especially for numerical and date fields.

