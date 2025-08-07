# Generates test reports (console, file, etc.)


def generate_report(results):
    print("=== Test Report ===")
    for test_type, tests in results.items():
        print(f"\n{test_type.upper()} Tests:")
        for test_name, result in tests.items():
            status = "PASS" if result["passed"] else "FAILED"
            print(f" {test_name}: {status}")
            if "id" in result:
                print(f"   Record ID: {result['id']}")
            if "token" in result:
                print(f"   Token: {result['token']}")
