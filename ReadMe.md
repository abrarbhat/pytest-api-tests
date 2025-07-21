# 🧪 Pytest API Automation Framework

This is a modular and scalable API test automation framework built using *Python* and *Pytest*. It is designed for clean code structure, reusability, and CI/CD friendliness.

## 🚀 Features Implemented

- ✅ Modular API wrapper using Python requests
- ✅ Fixtures for reusable components like auth token, config, and test data
- ✅ Dynamic payload creation using Faker
- ✅ JSON Schema validation with jsonschema
- ✅ Deep comparison of payload vs response using deepdiff
- ✅ Parallel test execution using pytest-xdist
- ✅ Test categorization with @pytest.mark (e.g., smoke, regression)
- ✅ Logging with rotation using Python's built-in logging
- ✅ HTML test reports via pytest-html
- ✅ Simple CLI with Makefile for common tasks (install, lint, run tests, etc.)

## 📁 Folder Structure


├── apis/                  # API wrapper classes
├── configs/               # YAML config files
├── fixtures/              # Custom pytest fixtures
├── schemas/               # JSON schemas for validation
├── tests/                 # Test cases
├── utils/                 # Utility classes (API client, helper functions)
├── logs/                  # Generated logs
├── reports/               # Test reports (HTML)
├── Makefile               # Commands to simplify usage
├── requirements.txt       # Python dependencies
├── pytest.ini             # Pytest config
└── README.md              # Project documentation


## 🔧 Installation

bash
git clone https://github.com/your-repo/pytest-api-framework.git
cd pytest-api-framework
make install


## ✅ Running Tests

### Run all tests:
bash
make test


### Run tests in parallel:
bash
make test-parallel


### Run with HTML report:
bash
make report


### Run a specific marker (e.g., smoke):
bash
pytest -m smoke


## 📝 Sample Makefile Commands

Makefile
install:
	pip install -r requirements.txt

test:
	pytest -v -s

test-parallel:
	pytest -n auto -v

report:
	pytest --html=reports/report.html --self-contained-html

lint:
	flake8 .


## 🔍 Next Steps

- ✅ Add test coverage reports (pytest-cov)
- ✅ Integrate with GitHub Actions for CI/CD
- ✅ Add contract testing via Pact
- ✅ Setup pre-commit hooks for code quality

## 🤝 Contributions
PRs and feedback are welcome!

## 📌 License
MIT License

---
Built with ❤️ by Abrar - Test Automation Architect | SDET | Automation | Quality Engineering
https://www.linkedin.com/in/abrar-bhat/
pytest -v tests/
run single test using 
pytest -v tests/test_departments.py


pytest tests/ --collect-only

pytest -n 4
pytest -n auto
pytest tests/ -n auto -v -s

pytest -m smoke
pytest -m "smoke or regression"
pytest -n auto -m smoke

pytest --html=reports/report.html --self-contained-html
