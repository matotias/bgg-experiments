from typing import Dict
from psycopg2 import connect
from psycopg2.extras import RealDictCursor


def using_query(credentials: Dict[str, str], query: str) -> RealDictCursor:
    connection = connect(**credentials)
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results
