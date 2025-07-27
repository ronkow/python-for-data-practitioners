# Python for Data Science

Welcome!

This course in Python programming is for people who have never written code in any programming language before.
It does not assume you know any programming terminology and concepts (not specific to Python).  
The only prerequisite is to have some basic math knowledge (e.g. prime numbers, sets, functions).
 
Learn programming like you would learn a foreign language - incrementally over months and years through regular reading and writing and short practices everyday.
Just as you do not master a foreign language in a few months, it will take you much longer to master your first programming language.
If you are a full-time student or have a day job, it is more effective to commit to 30 minutes of focused practice a day than to try to learn everything in one month.

The lessons cover all programming terminology, concepts and Python best practices.
We present code examples and provide coding exercises with solutions. You need to study code patterns and understand every line of code in the examples.
After that, type (or modify, if you like) and run the code to build your muscle memory.    

### WHERE DO I RUN PYTHON CODE?

You type and run code in an [Integrated Development Environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment). IDEs are software that help developers to manage software projects and write code efficiently.     

Given the many choices of IDEs for Python, installing and setting up your programming environment for the first time is a tricky process. There are also different ways to install Python (or, to be precise, the Python Interpreter, which is the software that checks and executes Python code). One option (which we do not recommend) is to install Python from the official [Python website](https://www.python.org/). This installation includes a basic interactive IDE called IDLE (Integrated Development and Learning Environment):

<!--![Python IDLE](./images/python_idle.png)-->
<!--<img src="./images/python_idle.png" width="800" alt="Python IDLE" style="border: 5px solid black;"> DOES NOT WORK-->
<kbd>
<img src="./images/python_idle.png" width="800" alt="Python IDLE">
</kbd>
<br><br>

### INSTALLING MINICONDA AND JUPYTERLAB

For a much better IDE and learning experience, we recommend using the [JupyterLab](https://jupyter.org) IDE. For ease of installing JupyterLab and other [Python packages](https://pypi.org/) for your future projects, download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main#should-i-install-miniconda-or-anaconda-distribution). Miniconda is one of two Python distributions (a collection of Python packages) from [Anaconda](https://www.anaconda.com/). By installing Miniconda, you will install the latest version of Python (version 3.13.5 at the time of writing this Introduction) and [Conda](https://docs.conda.io/en/latest/), the environment and package manager application. You will also install other packages that Python and Conda depends on (i.e. packages required for Python and Conda to work) and a small number of other useful packages, according to the [Miniconda website](https://www.anaconda.com/docs/getting-started/miniconda/main).

Once installed, you will see the following two applications (screenshot from Windows 10):

<kbd>
<img src="./images/miniconda3.png" width="260" alt="Python IDLE">
</kbd>
<br><br>

Open Anaconda Prompt, which is a command line application for managing your installations and environments. It shows the name of the default environment, which is `base`. Enter `conda list` at the prompt:

<kbd>
<img src="./images/conda_list.png" width="500" alt="Python IDLE">
</kbd>
<br><br>

This 'conda list' command lists all the Python packages installed in the `base` environment.

At this point, you may start to realise that installation and setup is a complex process. You may also start to wonder what exactly are packages and environments, and why there are so many packages installed by default.  

Missing from this list is JupyterLab, which we need to install.
