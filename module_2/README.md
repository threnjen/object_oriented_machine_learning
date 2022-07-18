# Module 2 Introduction

This is Module 2 in building a reusable, class-based machine learning framework.

In Module 1, we focused on preparing to code outside of Jupyter Notebook. We set up virtual environments with Pipenv, installed and configured VS Code, and added automatic Black formatting to our code.

In Module 2, we will focus on the following skills:
- Quick refresher of classes and object-oriented programming (or a quick introduction, but overall this is not intended as a tutorial about class-based programming)
- Building our base model class, onto which we we will build all future modules for EDA, visualizations, modeling, etc
- Introducing type hints and docstrings into our code

# Class Refresher (or brief introduction)

This section has a basic overview/refresher of classes. If you haven't seen a class before, follow along - but I cannot promise full understanding. However as the tutorial proceeds, the intricacies should become more clear.

A class can be considered a blueprint. It has its own set of functions (in a class we call these methods) that will all perform the same way no matter how many objects we make from the blueprint. It also has its own set of variables (in a class we call these attributes) that we can manipulate in the same way as global variables.

A common teaching example of a class object is a Dog. Let's make a sample class of type Dog, and make some different dog objects to explore how this works.

Here is our class Dog:

class Dog():

    def __init__(self, dog_type):
        self.type = dog_type
    
    def bark(self):
        print("WOOF!")
        print(self.type)

Classes ALWAYS start with a special method called the init. The init is always written as, at minimum, def __init__(self): and may contain nothing but a pass. A method like:
def __init__(self):
    pass
Is a perfectly valid init. It's not required to do anything. But what the init DOES do is, anytime you make an object using your CLASS blueprint, it will do all of the things inside of the init when it makes the object. You can think of the __init__ as the class setup function. In the Dog class init, we're passing an argument "dog_type" and setting a class attribute. Well talk more about how that works in a moment.

In the Dog class I am showing both an ATTRIBUTE and a METHOD. 
The ATTRIBUTE we made in the Dog class is self.type. Any variable inside a class that we preface with a "self." is available to all of the methods inside of the class.

Our class function is "def bark". Whenever we have a function inside a class, it is called a method.  You may see in the output of function "bark" that we reference the variable self.type, but *we did not have to pass it into the function*. This is one of the special ways that a class works. The class implicitly knows about all the self.xxxx attributes by having "self" as the first argument in all of its methods. The "self" that you see in all of the class methods is an *invisible argument* that you ignore when you are passing things to your class object. I'll show you what we mean shortly.

Let's make some dogs.

We are going to make a beagle.

beagle = Dog(dog_type = 'beagle')

We now have an instance of our object named beagle. We also make a different dog of a different type.

husky = Dog(dog_type = 'husky)

When we make a Dog instance of any type, that __init__ setup function gets run, and we can send it arguments just like any other function. You may recall before that I referrred to "self" as an *invisible* argument, meaning you always ignore it when sending arguments to a class method. The same is true for the __init__. But our dog init, in addition to self, calls for a dog_type argument. So we DO send it a dog_type argument when we make an instance of a dog.

Now that we have two different dogs, we can make them do the same thing by calling on their class method "bark"

> beagle.bark()
> WOOF!
> beagle

> husky.bark()
> WOOF!
> husky

When we call on the bark method with each dog, they woof and then report their dog_type. These aren't the same because even though they are both Dog class items, Dog is only a BLUEPRINT. A class definition is a BLUEPRINT that multiple similar objects to use.

We can also call our class attributes directly if we want to see them

> print(beagle.type)
> beagle

