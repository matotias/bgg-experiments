from typing import Dict, Any, List
from psycopg2 import connect
from psycopg2.extras import RealDictCursor


def using_query(credentials: Dict[str, str], query: str) -> List[Dict[str, Any]]:
    connection = connect(**credentials)
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return [dict(row) for row in results]
