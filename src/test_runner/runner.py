# Executes tests and collects results

from src.db.schema_parser import get_schema
from src.db.connector import get_db_connection
from src.test_generator.data_generator import generate_test_data
from src.test_generator.crud_tests import test_create, test_read, test_update, test_delete
from src.test_generator.login_tests import test_login, test_invalid_login

def run_tests(table_name, login_endpoint=None, username=None, password=None):
    results = {'crud': {}, 'login': {}}
    
    # CRUD Tests
    conn = get_db_connection()
    schema = get_schema(table_name, conn)
    test_data = generate_test_data(schema)
    
    # Create
    record_id = test_create(table_name, test_data)
    results['crud']['create'] = {'passed': record_id is not None, 'id': record_id}
    
    # Read
    if record_id:
        results['crud']['read'] = {'passed': test_read(table_name, record_id)}
        
    # Update
    if record_id:
        new_data = generate_test_data(schema)
        results['crud']['update'] = {'passed': test_update(table_name, record_id, new_data)}
    
    # Delete
    if record_id:
        results['crud']['delete'] = {'passed': test_delete(table_name, record_id)}
    
    conn.close()
    
    # Login Tests (if provided)
    if login_endpoint and username and password:
        passed, token = test_login(login_endpoint, username, password)
        results['login']['valid'] = {'passed': passed, 'token': token}
        passed, error = test_invalid_login(login_endpoint, username, 'wrong_password')
        results['login']['invalid'] = {'passed': passed, 'error': error}
    
    return results
