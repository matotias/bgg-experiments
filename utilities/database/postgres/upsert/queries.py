base_upsert_query = '''
INSERT INTO ${schema}.${table} (
    ${insert}
)
VALUES (%s)
ON CONFLICT ON CONSTRAINT "${primary_key}" DO UPDATE
SET
${set}
'''