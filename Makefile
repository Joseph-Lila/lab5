fix: isort lint
	echo "Good luck!"

lint:
	pylint src/

isort:
	isort src/ tests/
