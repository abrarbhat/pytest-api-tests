# Makefile

.PHONY: test test-parallel report lint format clean

test:
	pytest -v tests/

test-parallel:
	pytest -n auto -v tests/

report:
	pytest tests/ --html=reports/report.html --self-contained-html

lint:
	ruff check .

format:
	black .

clean:
	rm -rf __pycache__ .pytest_cache reports/*.html .mypy_cache
