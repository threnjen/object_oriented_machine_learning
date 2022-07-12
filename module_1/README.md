In Module 1, we focus on preparing our coding environment to move beyond Jupyter Notebook. In order to create a class based framework, the bones of that framework must be built in independent modules outside of a notebook. We can and will still work with our data from within Jupyter Notebook, but we will do so by importing our built modules into the notebook rather than filling our notebook with non-reusable code.

In Module 1 we will focus on the following skills:
- Setting up our project environment using Pipenv
- Picking out our code editor as we move beyond Jupyter Notebook
- Setting up code formatting with Black

#Using Pipenv for virtual environments

Environment management can be a confusing concept, but the objective is clear - keep your packages scoped per-project so that a package update in one project doesn't break another project, and so you can easily roll back if a package causes an error. You've likely heard of Anaconda and Miniconda for your environment management, and both of these are great environment packages. I have come to favor Pipenv for my environment manager because it creates a unique, understandable file in each directory where you have an environment, called a Pipfile, which details the packages in the environment. Each project directory has its own distinct Pipfile in the project root where I can easily see, at a glance, what packages I have installed for the environment and their versions if applicable.  Using Pipenv, your project will always be running with their own correct package installation, and the environment is easy to share with others simply by sharing the Pipfile. You can even use the Pipenv to manage different installs of Python.

Installing Pipenv is easy. Open your terminal and run pip install pipenv. Now, from within your project's root directory, run pipenv shell. An initial Pipfile will be created in the project directory, and you are up and running. Now, every time we open a command line in this directory, we run "pipenv shell" and the project environment will load with all of the packages installed in our Pipfile.

As we start out, the only packages installed in our Pipfile are a Python version. Let's get some initial packages installed for our tutorial. We will build on these as we go along. Let's install Jupyter Notebook and Pandas with the following lines:
First, make sure you are in your project's root directory, and have loaded the Pipenv with pipenv shell
pipenv install pandas
pipenv install notebook

As each package installs, the Pipfile is updated, and more detailed information written to Pipenv's proprietary file "Pipfile.lock". Don't mess with this file - Pipenv uses it for package versioning, and we're not intended to edit it directly.

#Picking out our code editor




