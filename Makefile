#!/bin/bash
.PHONY: astar_pathfinding snake

## General scripts
venv:
	( \
		python3.10 -m pip install --upgrade pip; \
		pip install virtualenv; \
		python3.10 -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)



## CI
test: venv
	( \
		source venv/bin/activate; \
		pip3.10 install coverage; \
		printf "\n---------\nLaunch tests..\n"; \
		python3.10 -m coverage run -m unittest; \
		printf "\nLaunch tests coverage analysis.."; \
		coverage report -m; \
		echo "Tests ended."; \
	)

synthax_snake: venv
	( \
		source venv/bin/activate; \
		pip install flake8; \
		printf "\n---------\nflake8 analyze.."; \
		flake8 snake --count --exit-zero --max-complexity=10 --max-line-length=120 --statistics; \
		echo "flake8 ended."; \
	)

synthax_astar_pathfinding: venv
	( \
		source venv/bin/activate; \
		pip install flake8; \
		echo "flake8 analyze :"; \
		flake8 astar_pathfinding --count --select=E9,F63,F7,F82 --show-source --statistics; \
		flake8 astar_pathfinding --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics; \
		echo "flake8 ended."; \
	)



## A* script
astar_pathfinding: venv test synthax_astar_pathfinding
	( \
		source venv/bin/activate; \
		python3.10 main.py astar; \
	)


## Snake game
snake: venv test synthax_snake
	( \
		source venv/bin/activate; \
		python3.10 main.py snake; \
	)

snake_build:
	docker build -f snake/Dockerfile . --tag snake:latest
	docker run snake:latest