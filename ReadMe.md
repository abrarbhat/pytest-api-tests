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