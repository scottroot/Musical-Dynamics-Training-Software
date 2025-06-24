.PHONY: help install install-dev test test-cov lint format clean build publish

help: ## Show this help message
	@echo "Musical Dynamics Training Software - Development Commands"
	@echo "========================================================"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

test: ## Run tests
	pytest tests/ -v

test-cov: ## Run tests with coverage report
	pytest tests/ --cov=musical_dynamics --cov-report=html --cov-report=term-missing

lint: ## Run linting checks
	flake8 src/ tests/
	mypy src/

format: ## Format code with black
	black src/ tests/

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

build: ## Build the package
	python -m build

publish: ## Publish to PyPI (requires twine)
	twine upload dist/*

check: ## Run all quality checks
	format
	lint
	test

dev-setup: ## Set up development environment
	install-dev
	format
	lint 