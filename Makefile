
.PHONY: dev
dev:
	pip install -e .
	pipenv install --dev
	pipenv shell