
##GETTING DATA

from google.cloud import bigquery

client = bigquery.Client()

# Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news",project ="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#List all the tables in "hacker_news" dataset
tables = list(client.list_tables(dataset))

#Print the table names in the "hacker_news" dataset
for table in tables:
    print(table.table_id)
    
# Construct a reference to the "comments" table    
table_ref = dataset_ref.table("comments")    

# API request - fetch the table
table = client.get_table(table_ref)

##QUERYING DATA

# Setting up a query to fetch the first 5 rows from the "comments" table
query = """
    SELECT *
    FROM `bigquery-public-data.hacker_news.comments`
    LIMIT 5
"""
# API request - run the query and convert the results to a pandas DataFrame
query_job = client.query(query)
results = query_job.to_dataframe()

##CHECKING QUERY COSTS

# Create a QueryJobConfig object to estimate size of query without running it
dry_run_config = bigquery.QueryJobConfig(dry_run=True)

# API request - dry run query to estimate costs
dry_run_query_job = client.query(query, job_config=dry_run_config)

# Print the number of bytes the query will process
print("This query will process {} bytes.".format(dry_run_query_job.total_bytes_processed))

##LIMITING QUERY COSTS

# Only run the query if it's less than 1 MB
ONE_MB = 1000*1000
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_MB)

# Set up the query (will only run if it's less than 1 MB)
safe_query_job = client.query(query, job_config=safe_config)

# API request - try to run the query, and return a pandas DataFrame
safe_query_job.to_dataframe()

### SQL QUERY'LERİ MySQL WORKBENCH DE YAZDIN ###