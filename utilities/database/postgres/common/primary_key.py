from string import Template
from typing import Dict
from .queries import index_query
from utilities.database.postgres import extract


def get_table_primary_key(schema: str, table: str, credentials: Dict[str, str]) -> str:
    query = Template(index_query).safe_substitute({'schema': schema, 'table': table})
    results = extract.using_query(credentials, query)
    if not len(results):
        raise ValueError("the table doesn't have a primary key")
    return results[0]['constraint_name']
