# Python for Data Science

## INTRODUCTION

This is a set of lessons in Python programming for people who have never written code in any programming language before.
We do not assume any prior knowledge of programming terminology and concepts (not specific to Python).
The only prerequisite is to have some basic math knowledge (e.g. prime numbers, sets, functions).
 
Learn programming like you would learn a foreign language - incrementally through regular reading, writing and short practices.
For most people, it takes years to be fluent in a foreign language. While programming is arguably easier, it will take months of consistent work to be fluent in your first programming language.
If you are a full-time student or have a day job, it is more effective to commit to 30 minutes of focused practice a day than to try to learn everything in one month.

The lessons cover all programming terminology, concepts and Python best practices.
We present code examples, explanations and provide coding exercises with solutions.
You need to study code patterns and understand every line of code in the examples.
After that, type (or modify, if you like) and run the code to build your muscle memory.    

### HOW DO I RUN PYTHON CODE?

To run Python code, you need to install the Python Interpreter, the software that checks and executes Python code. While it is possible to type and run Python code with just the Python Interpreter installed, it is much easier to write and run your code in an [Integrated Development Environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment). IDEs are software that help developers to manage software projects and write code efficiently.     

Given the different ways to install the Python Interpreter (which we will refer to as Python when it is clear that we are refering to the software, not the language) and the many choices of IDEs that support Python, installing and setting up Python and a suitable IDE for the first time is a tricky process. 

You can install Python from the official [Python website](https://www.python.org/). This installation includes a basic interactive IDE called IDLE (Integrated Development and Learning Environment):

<!--![Python IDLE](./images/python_idle.png)-->
<!--<img src="./images/python_idle.png" width="800" alt="Python IDLE" style="border: 5px solid black;"> DOES NOT WORK-->
<kbd>
<img src="./images/python_idle.png" width="700" alt="Python IDLE">
</kbd>
<br><br>

Although installing Python is easy this way and IDLE is easy to use, we do not recommend this option for beginners. 

### INSTALLING MINICONDA AND JUPYTERLAB
For a much better IDE and learning experience, we recommend using [JupyterLab](https://jupyter.org), an IDE that runs in a web browser. We also recommend installing
[conda](https://docs.conda.io/en/latest/) for managing virtual environments and [pip](https://pypi.org/project/pip/) for installing other Python packages.

The two-step installation process will be as follows:
- Download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main#should-i-install-miniconda-or-anaconda-distribution). By installing Miniconda, you will install the latest version of Python (version 3.13.5 at the time of writing this guide), conda and pip at the same time.
- Install JupyterLab using pip.

At this point, you may be wondering: What is a [virtual environment](https://docs.python.org/3/library/venv.html)? What is a [Python packages](https://pypi.org/)? What is Miniconda? Let's first proceed with our installation. We will explain these terms along the way.

When Miniconda is installed, you will see the following two applications (screenshot from Windows 10):

<kbd>
<img src="./images/miniconda3.png" width="260" alt="Python IDLE">
</kbd>
<br><br>

Open Anaconda Prompt, which is a command line application. It shows the name of the default environment, which is `base`. Enter `conda list` at the prompt:

<kbd>
<img src="./images/conda_list.png" width="500" alt="Python IDLE">
</kbd>
<br><br>

This `conda list` command lists all the Python packages installed in the default virtual environment named `base`. The complete list is as follows:

```
Name                        Version          Build               Channel
anaconda-anon-usage           0.7.1            py313hfc23b7f_100 
anaconda_powershell_prompt    1.1.0            haa95532_1  
anaconda_prompt               1.1.0            haa95532_1
annotated-types               0.6.0            py313haa95532_0
archspec                      0.2.3            pyhd3eb1b0_0
boltons                       25.0.0           py313haa95532_0
brotlicffi                    1.0.9.2          py313h5da7b33_1
bzip2                         1.0.8            h2bbff1b_6
ca-certificates               2025.2.25        haa95532_0
certifi                       2025.7.14        py313haa95532_0
cffi                          1.17.1           py313h827c3e9_1
charset-normalizer            3.3.2            pyhd3eb1b0_0
colorama                      0.4.6            py313haa95532_0
conda                         25.5.1           py313haa95532_0
conda-anaconda-telemetry      0.2.0            py313haa95532_1
conda-anaconda-tos            0.2.1            py313haa95532_0
conda-content-trust           0.2.0            py313haa95532_1
conda-libmamba-solver         25.4.0           pyhd3eb1b0_0
conda-package-handling        2.4.0            py313haa95532_0
conda-package-streaming       0.12.0           py313haa95532_0
cpp-expected                  1.1.0            h214f63a_0
cryptography                  45.0.3           py313h51e0144_0
distro                        1.9.0            py313haa95532_0
expat                         2.7.1            h8ddb27b_0
fmt                           9.1.0            h6d14046_1
frozendict                    2.4.2            py313haa95532_0
idna                          3.7              py313haa95532_0
jsonpatch                     1.33             py313haa95532_1
jsonpointer                   2.1              pyhd3eb1b0_0
libarchive                    3.7.7            h9243413_0
libcurl                       8.14.1           ha9f67de_0
libffi                        3.4.4            hd77b12b_1
libiconv                      1.16             h2bbff1b_3
libmamba                      2.0.5            hcd6fe79_1
libmambapy                    2.0.5            py313h214f63a_1
libmpdec                      4.0.0            h827c3e9_0
libsolv                       0.7.30           hf2fb9eb_1
libssh2                       1.11.1           h2addb87_0
libxml2                       2.13.8           h866ff63_0
lz4-c                         1.9.4            h2bbff1b_1
markdown-it-py                2.2.0            py313haa95532_1
mdurl                         0.1.0            py313haa95532_0
menuinst                      2.3.0            py313h5da7b33_0
nlohmann_json                 3.11.2           h6c2663c_0
openssl                       3.0.16           h3f729d1_0
packaging                     24.2             py313haa95532_0
pcre2                         10.42            h0ff8eda_1
pip                           25.1             pyhc872135_2
platformdirs                  4.3.7            py313haa95532_0
pluggy                        1.5.0            py313haa95532_0
pybind11-abi                  5                hd3eb1b0_0
pycosat                       0.6.6            py313h827c3e9_2
pycparser                     2.21             pyhd3eb1b0_0
pydantic                      2.11.7           py313haa95532_0
pydantic-core                 2.33.2           py313h215eeae_0
pygments                      2.19.1           py313haa95532_0
pysocks                       1.7.1            py313haa95532_0
python                        3.13.5           h286a616_100_cp313
python_abi                    3.13             0_cp313
reproc                        14.2.4           hd77b12b_2
reproc-cpp                    14.2.4           hd77b12b_2
requests                      2.32.4           py313haa95532_0
rich                          13.9.4           py313haa95532_0
ruamel.yaml                   0.18.10          py313h827c3e9_0
ruamel.yaml.clib              0.2.12           py313h827c3e9_0
setuptools                    78.1.1           py313haa95532_0
simdjson                      3.10.1           h214f63a_0
spdlog                        1.11.0           h59b6b97_0
sqlite                        3.50.2           hda9a48d_1
tk                            8.6.14           h5e9d12e_1
tqdm                          4.67.1           py313h4442805_0
truststore                    0.10.0           py313haa95532_0
typing-extensions             4.12.2           py313haa95532_0
typing-inspection             0.4.0            py313haa95532_0
typing_extensions             4.12.2           py313haa95532_0
tzdata                        2025b            h04d1e81_0
ucrt                          10.0.22621.0     haa95532_0
urllib3                       2.5.0            py313haa95532_0
vc                            14.3             h2df5915_10
vc14_runtime                  14.44.35208      h4927774_10
vs2015_runtime                14.44.35208      ha6b5a95_10
wheel                         0.45.1           py313haa95532_0
win_inet_pton                 1.1.0            py313haa95532_0
xz                            5.6.4            h4754444_1
yaml-cpp                      0.8.0            hd77b12b_1
zlib                          1.2.13           h8cc25b3_1
zstandard                     0.23.0           py313h4fc1ca9_1
zstd                          1.5.6            h8880b57_0
```


Missing from this list is JupyterLab, which we need to install. Enter `pip install jupyterlab` at the prompt:

<kbd>
<img src="./images/pip_install_jupyterlab.png" width="500" alt="Python IDLE">
</kbd>
<br><br>


### VIRTUAL ENVIRONMENT
A virtual environment is an isolated workspace for a software project. Within a project's virtual environment, you install a specific version of Python and the [Python packages](https://pypi.org/) required for the project using either conda or [pip](https://pypi.org/project/pip/) 


<!--For ease of installing JupyterLab and other [Python packages](https://pypi.org/) for your future projects--> 
<!--download and install [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main#should-i-install-miniconda-or-anaconda-distribution). 
Miniconda is one of two Python distributions (a collection of Python packages) from [Anaconda](https://www.anaconda.com/).-->

<!--By installing Miniconda, you will install the latest version of Python (version 3.13.5 at the time of writing this guide) and [Conda](https://docs.conda.io/en/latest/), the environment and package manager application, at the same time. You will also install other packages that Python and Conda depend on (i.e. packages required for Python and Conda to work) and a small number of other useful packages (according to the [Anaconda guide](https://www.anaconda.com/docs/getting-started/miniconda/main)).-->




This command downloads and installs JupyterLab (and other packages it depends on) from the [Python Package Index](https://pypi.org/project/jupyterlab/), a repository of all Python packages created by developers all over the world. Other options for installing JupyterLab is provided in [Python Package Index](https://pypi.org/project/jupyterlab/), including the command `conda install -c conda-forge jupyterlab`, which downloads and installs JupyterLab from the [Conda Forge](https://conda-forge.org/) repository.

To type and run your code interactively, use Notebooks. Select `File` > `Notebook` to open a new Notebook, then select the default option (Python 3):

<kbd>
<img src="./images/jupyterlab_notebook_select.png" width="600" alt="Python IDLE">
</kbd>
<br><br>

In the first cell, enter your code and click on the Run button (or use the keyboard shortcut `Shift` `Enter`):

<kbd>
<img src="./images/jupyterlab_notebook_hello.png" width="600" alt="Python IDLE">
</kbd>
<br><br>

You are now ready for your first lesson.

<!--At this point, you may also start to wonder what exactly are packages and environments, and why there are so many packages installed by default.  -->


