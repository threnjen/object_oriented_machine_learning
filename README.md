As an aspiring data scientist or even a production level contributor, it's possible that many of your projects entail spinning up a Jupyter Notebook and writing a hard-coded project from start to finish. Maybe you'll use a few functions here and there for reusability, but generally, the project is fully self-contained. When you start your next project, you may find yourself hunting through an older project for interesting code snippets - what was that function that made that cool visual? How did I engineer that particular feature again? What was that method that I used to do that...other thing?

In this series, we are going to build a class-based machine learning framework which is reusable, expandable, and can accomodate both regression and classification problems. As we work through our build we will focus on several coding best-practices to make our code clean and understandable for our future self, including:
- [virtual environments](https://pipenv.pypa.io/en/latest/)
- [type hints](https://docs.python.org/3/library/typing.html)
- [proper docstrings](https://peps.python.org/pep-0257/)
- [auto-formatting](https://github.com/psf/black)
- [testing](https://docs.pytest.org/en/7.1.x/)

At the end of 7 modules we will have an extensible class-based modeling framework into which we can easily plug a fresh dataset and add new and interesting methods.

The only base assumptions as we start the project are an install of [Python 3.9 or greater](https://www.python.org/downloads/) on your machine--properly added to the path--as well as a passing familiarity/[introduction to Python classes](https://realpython.com/python3-object-oriented-programming/). You'll also need to have the [pip package downloader](https://pypi.org/project/pip/) installed.

The GitHub repo for this project is [here](https://github.com/threnjen/object_oriented_machine_learning)
Each module section includes a tutorial notebook and all related code for the module's lesson.

[Module 1](https://github.com/threnjen/object_oriented_machine_learning/blob/main/module1/module_1.ipynb):
- Setting up our project environment using [Pipenv](https://pipenv.pypa.io/en/latest/)
- Picking out our code editor as we move beyond Jupyter Notebook
- Setting up code formatting with [Black](https://github.com/psf/black)

[Module 2](https://github.com/threnjen/object_oriented_machine_learning/blob/main/module2/module_2.ipynb):
- Quick refresher of classes and object-oriented programming (or a quick introduction, but this is not intended as a tutorial about class-based programming)
- Building our base model class with an initial exploratory method
- Introducing docstrings into our code

[Module 3](https://github.com/threnjen/object_oriented_machine_learning/blob/main/module3/module_3.ipynb):
- Building an EDA handler class
- Integrating our EDA handler into our BaseModel

[Module 4](https://github.com/threnjen/object_oriented_machine_learning/blob/main/module4/module_4.ipynb):
- Understanding the concept of an abstract class
- Setting up a Regression abstract class
- Introducing type hints into our code

