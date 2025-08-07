📁 Auto CRUD Test Builder - File Structure
===============================================

auto_tester/
├── 📁 .git/                          # Git repository metadata
├── 📄 .gitignore                     # Git ignore rules
├── 📄 README.md                      # Project documentation
├── 📄 main.py                        # 🚀 Entry point - CLI interface
├── 📄 requirements.txt               # Python dependencies
│
├── 📁 config/                        # Configuration files
│   ├── 📄 db_config.yaml            # Database credentials (ignored by git)
│   └── 📄 db_config.yaml.template   # Database config template
│
├── 📁 src/                          # 🧠 Main source code
│   ├── 📄 __init__.py               # Package initialization
│   │
│   ├── 📁 db/                       # 🗄️ Database operations
│   │   ├── 📄 __init__.py
│   │   ├── 📄 connector.py          # Database connection logic
│   │   └── 📄 schema_parser.py      # Schema discovery & analysis
│   │
│   ├── 📁 test_generator/           # 🧪 Test creation engine
│   │   ├── 📄 __init__.py
│   │   ├── 📄 crud_tests.py         # CRUD test generation
│   │   ├── 📄 data_generator.py     # Realistic test data creation
│   │   └── 📄 login_tests.py        # Authentication test generation
│   │
│   ├── 📁 test_runner/              # ⚡ Test execution
│   │   ├── 📄 __init__.py
│   │   └── 📄 runner.py             # Test orchestration & execution
│   │
│   ├── 📁 reporting/                # 📊 Results & analytics
│   │   ├── 📄 __init__.py
│   │   └── 📄 reporter.py           # Test report generation
│   │
│   └── 📁 utils/                    # 🛠️ Helper functions
│       ├── 📄 __init__.py
│       └── 📄 helpers.py            # Utility functions & logging
│
└── 📁 tests/                        # ✅ Unit & integration tests
    ├── 📄 __init__.py
    ├── 📄 test_connector.py         # Database connector tests
    ├── 📄 test_schema_parser.py     # Schema parser tests
    ├── 📄 test_data_generator.py    # Data generation tests
    ├── 📄 test_crud.py              # CRUD functionality tests
    └── 📄 test_login.py             # Login functionality tests

═══════════════════════════════════════════════════════════════
