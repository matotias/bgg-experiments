from sqlalchemy.engine import create_engine
from datetime import datetime, timezone
from sqlalchemy import Table, MetaData


def load_data(credentials_path: str, dataset: str, table: str, data: list) -> None:
    engine = create_engine('bigquery://', credentials_path=credentials_path)
    table = Table(f'{dataset}.{table}', MetaData(bind=engine), autoload=True)
    conn = engine.connect()
    conn.execute(table.insert(data))


def format_data(data: list, run_id: str, country: str) -> list:
    return [
        {
            'run_id': run_id,
            'username': value,
            'country': country,
            'inserted_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc)
        }
        for value in data
    ]
