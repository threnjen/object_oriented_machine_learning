As an aspiring data scientist or even a production level contributor, it's possible that many of your projects entail spinning up a Jupyter Notebook and writing a hard-coded project from start to finish. Maybe you'll use a few functions here and there for reusability, but generally, the project is fully partitioned. Then when you start your next project, you may find yourself hunting through an older project for interesting code snippets - what was that function that made that cool visual? How did I engineer that particular feature again? What was that method that I used to do that... one thing?

In this series, we are going to build a class-based machine learning framework which is reusable, expandable, and can accomodate both regression and classification problems. As we work through our build we will focus on several coding best-practices to make our code clean and understandable for our future self, including: virtual environments, type hints, proper docstrings, auto-formatting, and testing. At the end of 7 modules we will have an extensible class-based modeling framework into which we can easily plug a fresh dataset and add new and interesting methods.

The only base assumption as we start the project are an install of Python 3.9 or greater on your machine, properly added to the path, as well as a passing familiarity/introduction to Python classes. You'll also need to have the pip package downloader installed.

In Module 1:
- Setting up our project environment using Pipenv
- Picking out our code editor as we move beyond Jupyter Notebook
- Setting up code formatting with Black

Module 2:
- Quick refresher of classes and object-oriented programming (or a quick introduction, but this is not intended as a tutorial about class-based programming)
- Building our base model class, onto which we we will build all future modules for EDA, visualizations, modeling, etc
- Introducing type hints and docstrings into our code

Module 3:
- Understanding the concept of an abstract class
- Setting up a Regression abstract class
- Building an initial exploratory method

