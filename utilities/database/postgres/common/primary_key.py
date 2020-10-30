from string import Template
from typing import Dict
from utilities.database.postgres.common.queries import index_query
from utilities.database.postgres import extract


def get_table_primary_key(schema: str, table: str, credentials: Dict[str, str]) -> str:
    query = Template(index_query).safe_substitute({'schema': schema, 'table': table})
    results = extract.using_query(credentials, query)
    return results[0]['constraint_name'] if len(results) > 0 else None
