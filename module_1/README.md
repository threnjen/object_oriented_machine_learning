# Module 1 Introduction

In Module 1, we focus on preparing our coding environment to move beyond Jupyter Notebook. In order to create a class based framework, the bones of that framework must be built in independent modules as pure .py files. We can and will work with our data from within Jupyter Notebook, but we will do so by importing our built modules into the notebook rather than filling our notebook with non-reusable code.

In Module 1 we will focus on the following skills:
- Setting up our project environment using Pipenv
- Picking out our code editor as we move beyond Jupyter Notebook
- Setting up code formatting with Black

# Using Pipenv for virtual environments

Environment management can be confusing, but the objective is clear - keep your packages scoped per-project so that a package update/install in one project doesn't break another project, and so you can easily roll back if a package causes an error. You've likely heard of Anaconda and Miniconda for your environment management, and both of these are great environment packages. I have come to favor Pipenv for my environment manager because it creates a unique, understandable file in each directory where you have an environment, called a Pipfile, which details the packages in the environment. Each project directory has its own distinct Pipfile in the project root where I can easily see, at a glance, what packages I have installed for the environment and their versions if applicable.  Using Pipenv, your project will always be running with its own correct package installation, and the environment is easy to share with others simply by sharing the Pipfile. You can even use the Pipenv to manage different installs of Python.

Installing Pipenv is easy. Open your terminal and run pip install pipenv. Now, from within your project's root directory, run pipenv shell. An initial Pipfile will be created in the project directory, and you are up and running. Now, every time we open a command line in this directory, we run "pipenv shell" and the project environment will load with all of the packages installed in our Pipfile.

As we start out, the only package installed in our Pipfile is a Python version. Let's get some initial packages installed for our tutorial series. We will build on these as we go along. First, make sure you are in your project's root directory, and have loaded the Pipenv with pipenv shell. We'll install Jupyter Notebook and Pandas with the following lines:
pipenv install pandas
pipenv install notebook

As each package installs, the Pipfile is updated, and more detailed information written to Pipenv's proprietary file "Pipfile.lock". Don't mess with either Pipfile - Pipenv uses these for package versioning, and we're not intended to edit them directly.

# Picking out our code editor

In order to create our class-based framework, we'll need to build modules as pure .py files, which means we'll need a dedicated code editor. My hands-down favorite is Visual Studio Code, which is free and works on both Windows and Mac. But any dedicated code editor such as Notebook++, Sublime, etc will do. I favor VS Code because it has an extensive library of available extensions, including a Jupyter Notebook extension which allows us to run our notebooks from within the program. It also has excellent GitHub extension integration, which comes in very handy later on when you want to publish your projects for others to see!

Since I use VS Code, the instructions I give will be related to that program. I trust you can Google to figure out how to accomplish similar things if your program of choice is different.

Install VSCode, start it up, and open your project folder. Now under file hit "Save Workspace As" and save a workspace in your root project folder to set up your VSCode workspace.

You'll now want a few handy extensions for our project, which you can access by hitting "Extensions" in the side tab. Search up and install: Python, Pylance, Jupyter, and autoDocstring. I'm also a fan of indent-rainbow which shows your indent levels by color. If you plan to integrate with GitHub from VSCode rather than command line, you'll also want to install GitHub Pull Requests and Issues, and GitLens. These are the only extensions that I have needed for VS Code, but feel free to hunt for others!

# Setting up code formatting with Black

The last step of Module 1 is the first of our good code practices - using code formatting. We will configure VS Code to automatically format our code with the popular Black formatter. Code formatting makes your code consistent and readable, and aligns it automatically to a proper PEP-8 standard. Other people (as well as you!) will be able to easily read and follow your code blocks.

Open up your terminal, run pipenv shell as always, and enter pipenv install black

In VS Code, we'll set up black to automatically format our files on save. Open VS Code settings (in Windows, click the gear icon located at the lower left and select Settings). The Settings will open up in your main screen area. We're setting up two things:
- Pull down the "Text Editor" section and select "Formatting". Click "Format on Save:
- In the search box at top, enter "python formatting provider". Pull down the python formatting provider and select Black.

Now, your files will be auto-formatted with Black on save. Easy!

# Next Steps

We have our virtual environment set up, we have our code editor ready to go, and we've prepped for our first good coding habit - consistent formatting (and we don't even have to work more for this one!). We're ready to start coding in Module 2, where we will have a refresher (or simple introduction) to classes, and start building our model object.


