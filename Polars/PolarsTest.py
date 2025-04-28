import polars as pl

# Create a DataFrame
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "New York"]
})

print(df)

# # Create a LazyFrame for optimized query execution
# lazy_df = df.lazy()

# # Perform operations on the LazyFrame
# result_lazy = (
#     lazy_df.filter(pl.col("age") > 25)
#     .group_by("city")
#     .agg(pl.count().alias("count"))
#     .collect()  # Execute the query
# )

# print(result_lazy)