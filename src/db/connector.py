import psycopg2
import yaml

def load_config():
    with open("config/db_config.yaml", "r") as file:
        return yaml.safe_load(file)
    
def get_db_connection():
    config = load_config()['database']
    try:
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['name'],
            user=config['user'],
            password=config['password']   
        )
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        raise
    