# Generates test data based on schema
from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_test_data(schema):
    test_data = {}
    for column in schema:
        col_name = column['column_name']
        data_type = column['data_type']
        max_length = column['max_lentgh']
        
        if data_type in ['varchar', 'character varying']:
            test_data[col_name] = fake.word()[:max_length] if max_length else fake.word()
        elif data_type in ['integer', 'bigint']:
            test_data[col_name] = random.randint(1, 1000)
        elif data_type == 'date':
            test_data[col_name] = fake.date()
        elif data_type == 'timestamp without time zone':
            test_data[col_name] = datetime.now()
        elif column['is_nullable']:
            test_data[col_name] = None
        else:
            test_data[col_name] = 'default'  # Fallback for unhandled types
    return test_data