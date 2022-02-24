Python Quick Projects
===


| Linter |                                                                         CI/CD and testing                                                                         |                                                                                                Test Coverage                                                                                                 |
|:---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Thibault-Santonja/Python_Quick_Projects.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Thibault-Santonja/Python_Quick_Projects/context:python) | [![Build Status](https://circleci.com/gh/Thibault-Santonja/Python_Quick_Projects.svg?style=svg)](https://circleci.com/gh/Thibault-Santonja/Python_Quick_Projects) | [![Code Coverage](https://img.shields.io/codecov/c/github/Thibault-Santonja/Python_Quick_Projects.svg?style=for-the-badge)](https://codecov.io/github/Thibault-Santonja/Python_Quick_Projects?branch=master) |



The purpose of this repository is to regroup a lot of fun and quick Python project that I made on my free time to level
up on algorithm (A* pathfinding, Voronoi...), on software development (design patterns, logger...) and in Python
(and some of its libraries).


Another purpose of this project is to try some CI/CD tools:
- Git : clean commit and history
- Makefile
- Docker
- Testing using :
  - Unittest, PyTest
  - Codecov (coverage analysis)
- Code quality using :
  - Flake8 (linter)
  - LGTM (analyze the code and give it a notation. It acts like a linter)
- CI / CD using :
  - GitHub action (commented now and replaced by CircleCI)
  - Circle CI
- Methodology like :
  - Test Driven Development
  - Branching Strategies (not for the moment, but I will) and Trunk-Based (maybe I'll try)
  
> To test next : Jenkins, Sonar, Jasine


## Run

To run these scripts, you can use the Makefile and run the command link with the following projects (`make <project_name>`).


### A* Pathfinding
```shell
make astar_pathfinding
```
I just want to implement an algorithm that we quickly mentioned in class. I've used PyGame.

### Snake
```shell
make snake
```
Just a first try of PyGame, not y best project. I've used PyGame.

### Brick breaker
```shell
make brick_breaker
```
A little challenge to spend an afternoon doing a quick Bick Breaker game. I've used PyGame.

---
*Thibault Santonja*<br/>
*2021*
