from typing import Dict, List
from psycopg2 import connect
from string import Template


def get_table_columns(schema: str, table: str, credentials: Dict[str, str]) -> List[str]:
    connection = connect(**credentials)
    query = Template('SELECT * FROM ${schema}.${table} LIMIT 0').safe_substitute({'schema': schema, 'table': table})
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    connection.close()
    return columns
