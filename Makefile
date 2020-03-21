
.PHONY: dev
dev:
	pipenv install --dev
	pipenv shell
	pip install -e .