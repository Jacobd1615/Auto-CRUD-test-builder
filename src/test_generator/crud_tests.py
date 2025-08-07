# CRUD test case generation
from src.db.connector import get_db_connection

def test_create(table_name, test_data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        columns = ', '.join(test_data.keys())
        placeholders = ', '.join(['%s'] * len(test_data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders}) RETURNING id"
        cursor.execute(query, list(test_data.values()))
        result = cursor.fetchone()
        conn.commit()
        return result[0] if result else None
    finally:
        conn.close()

def test_read(table_name, record_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE id = %s"
        cursor.execute(query, (record_id,))
        return cursor.fetchone() is not None
    finally:
        conn.close()

def test_update(table_name, record_id, test_data):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        updates = ', '.join([f"{key} = %s" for key in test_data.keys()])
        query = f"UPDATE {table_name} SET {updates} WHERE id = %s"
        cursor.execute(query, list(test_data.values()) + [record_id])
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

def test_delete(table_name, record_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE id = %s"
        cursor.execute(query, (record_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()