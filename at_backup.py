from airtable import Airtable
from datetime import datetime
from pathlib import Path
from collections import namedtuple
import csv
import os


"""
Note that Airtable Python Wrapper assumes you've stored your Airtable API key in an environment variable 
called AIRTABLE_API_KEY. See https://airtable-python-wrapper.readthedocs.io/en/master/authentication.html 
for more information on this.
"""
# TODO Add error handling (Incorrect or missing API Key or base key, no internet connection, etc)


def main():
    # Base key is the string of alphanumeric characters directly after
    # 'api.airtable.com' in your API query.
    base_key = os.environ['AIRTABLE_BASE_KEY']
    Table = namedtuple('Table', 'name, sort_value')
    tables = [Table(name='YOUR TABLE NAME', sort_value='NAME OF FIELD TO SORT CSV BY'),
              Table(name='OTHER TABLE NAME', sort_value='NAME OF FIELD TO SORT CSV BY'), ]
    for table in tables:
        table_backup(base_key, table)


def get_fields(table_name):
    filename = Path(f'field-files/{table_name}-fields.txt')
    with open(filename, 'r') as f:
        fields = f.readlines()
        fields = [field.strip() for field in fields]  # To remove newline characters
    return fields


def table_backup(base_key, table):
    fields = get_fields(table.name)
    airtable = Airtable(base_key, table.name)
    results = airtable.get_all(sort=table.sort_value)  # Sort is optional, but makes CSV easier to read
    data = [item['fields'] for item in results]
    filepath = Path('PATH/TO/YOUR/BACKUPS/FOLDER')  # Use forward slashes!
    now = datetime.strftime(datetime.now(), "%b-%d-%Y-%H%M")
    with open(f'filepath / {table.name}-Backup-{now}.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fields, restval='')
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == '__main__':
    main()


