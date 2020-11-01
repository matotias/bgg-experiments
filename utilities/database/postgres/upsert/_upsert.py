from ..common.columns import get_table_columns
from ..common.primary_key import get_table_primary_key
from psycopg2.extras import execute_values
from psycopg2 import connect
from .queries import base_upsert_query
from string import Template
from typing import Dict, List, Any
from copy import deepcopy
import logging


# TODO: instead of expecting all columns and excluding a few add the option to only write on the ones provided
def upsert_data(data: List[Dict[str, Any]], schema: str, table: str, credentials: Dict[str, str],
                excluded_columns: List[str] = ()) -> None:
    table_columns = filter_list(get_table_columns(schema, table, credentials), excluded_columns)
    query = _generate_upsert_query(schema, table, credentials, table_columns)
    template = _generate_values_template(table_columns)
    transformed_data = [add_missing_keys(row, table_columns) for row in data]
    logging.info('running the following query:')
    logging.info(query)
    load_data(credentials, query, transformed_data, template)


def _generate_upsert_query(schema, table, credentials, table_columns):
    primary_key = get_table_primary_key(schema, table, credentials)
    insert_string = _generate_insert_string(table_columns)
    set_string = _generate_set_string(table_columns)
    return Template(base_upsert_query).safe_substitute({
        'schema': schema,
        'table': table,
        'primary_key': primary_key,
        'insert': insert_string,
        'set': set_string
    })


# TODO: add option to pass reserved columns
def _generate_insert_string(columns: List[str]) -> str:
    separator = ',\n\t'
    return f"{separator.join(columns)}"


# TODO: add option to pass reserved columns
def _generate_values_template(columns: List[str]) -> str:
    return ', '.join([f'%({column})s' for column in columns])


# TODO: add option to pass reserved columns
# TODO: add option to pass a column mapping?
def _generate_set_string(columns):
    return ',\n\t'.join([f'{column} = excluded.{column}' for column in columns])


def add_missing_keys(dictionary: Dict[Any, Any], keys: List[Any]) -> Dict[Any, Any]:
    output = deepcopy(dictionary)
    for key in keys:
        if key not in dictionary:
            output[key] = None
    return output


def load_data(credentials: Dict[str, str], query: str, data: List[Dict[str, Any]], template: str) -> None:
    connection = connect(**credentials)
    cursor = connection.cursor()
    execute_values(cursor, query, data, template=template)
    connection.commit()


def filter_list(a_list: List[str], excluded: List[str]):
    return list(filter(lambda x: x not in excluded, a_list))
