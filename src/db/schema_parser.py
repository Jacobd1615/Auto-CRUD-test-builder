# Schema discovery and parsing logic
def get_schema(table_name, conn):
    try:
        cursor = conn.cursor()
        query = """
        SELECT column_name, data_type, is_nullable, character_maximum_length
        FROM information_schema.columns
        WHERE table_name = %s;
        """
        cursor.execute(query, (table_name,))
        schema = [
            {
                'column_name': row[0],
                'data_type': row[1],
                'is_nullable': row[2] == 'YES',
                'max_length': row[3]
            }
            for row in cursor.fetchall()
        ]
        return schema
    except Exception as e:
        print(f"Schema praising failed: {e}")
        raise
    finally:
        cursor.close()