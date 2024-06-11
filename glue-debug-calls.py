The glue GetTables with expression set to 'tableName' seems to fire many GetTables API calls proportional to number of tables in the database. Assume that database has 5000 tables, Even though final result is one, it would be firing 50 GetTables API calls (out of only has result.)

import boto3
#boto3.set_stream_logger(name='botocore')

next_token = ""
client = boto3.client('glue',region_name='us-east-1')
crawler_tables = []
i = 0
while True:
  response = client.get_tables(CatalogId = 'xxxxxx',DatabaseName = 'abc', Expression = "ref_xxxxxx" ,NextToken = next_token)
  size = 0 
  for tables in response['TableList']:
    for columns in tables['StorageDescriptor']['Columns']:
        crawler_tables.append(tables['Name'] + '.' + columns['Name'])
    size = size + 1
  next_token = response.get('NextToken')
  i = i + 1
  print(f" {i}th iteration : {next_token} : {size}")
  if next_token is None:
    break
print(len(crawler_tables))



Output: Below is the output showing number of GetTables being made and number of tables result in each paginated response.
