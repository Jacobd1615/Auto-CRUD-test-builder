# Entry point for running the auto-tester (CLI or script)
from src.test_runner.runner import run_tests
from src.reporting.reporter import generate_report

def main():
    table_name = input("Enter table/model name (e.g., Customer): ")
    login_endpoint = input("Enter login API endpoint (or press Enter to skip): ")
    username = input("Enter test username (or press Enter to skip): ") if login_endpoint else None
    password = input("Enter test password (or press Enter to skip): ") if username else None
    
    results = run_tests(table_name, login_endpoint or None, username, password)
    generate_report(results)

if __name__ == "__main__":
    main()