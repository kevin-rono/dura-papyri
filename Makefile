.PHONY: quality style

check_dirs := bin src

quality:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)

style:
	black $(check_dirs)
	isort $(check_dirs)