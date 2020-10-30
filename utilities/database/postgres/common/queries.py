index_query = '''
select constraint_name
FROM information_schema.table_constraints tc
WHERE true
    and constraint_type = 'PRIMARY KEY'
    and tc.table_name = '${table}'
    and tc.table_schema='${schema}';
'''
