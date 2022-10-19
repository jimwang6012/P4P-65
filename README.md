<h1 align="center">
  Towards Automatically Evaluating Stackoverflow.com Code Snippets
  <br>
</h1>
<h4 align="center">Project 65</h4>
<p align="center">
<br>

Project 65 by SV Singh & Jimmy Wang

This tool allows for the automatic execution of StackOverflow Java code snippets and the identification of outliers based on correctness and execution time.

## Prerequisites

- Set up a virtual machine capable of running Linux. More information [here](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview).
  
  > Note: For our experiments Ubuntu 22.04.1 LTS was used

- Install Python 3.x from [here](https://www.python.org/downloads/).
  
  > Note: For our experiments Python3.7 was used

- Install JDK 18 from [here](https://www.oracle.com/java/technologies/javase/jdk18-archive-downloads.html).
  
  > Note: For our experiments Java 18.0.2.1 was used
  
## Required Modules

Numerous Python modules will need to be installed to run the tool. 

- Install the modules by executing `pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`
  
  > Note: For our experiments the specific modules we used were `pysqlite3 0.4.7`, `numpy 1.20.3` and `tabulate 0.9.0`

## Dataset

- The dataset used is sourced from [here](https://archive.org/download/stackexchange).
  
- You must download the `stackoverflow.com-Posts.7z` file.
  
  > Note: This dataset contains the publicly accessible StackOverflow posts as of 2022.

- The `stackoverflow.com-Posts.7z` folder should be extracted and the `Posts.xml` file inside must be placed into the `./PostParser` folder.
  
  > Note: A sub-set of this data can also be used
  
## Running the tool

In order to run the tool, follow these steps

- Open your terminal and set the working directory to `./GenerateAndRunTests`.
- Execute the commands `chmod u+r+x ./bin/pmd.bat` and `chmod u+r+x ./bin/run.sh` in the terminal to give access permission to the static analysis tools.
- Set the working directory back to `./P4P-65`.
- Execute the CLI command `python3 CSEval.py -flag` where `-flag` specifies which module to run
  
  > Note: Modules and flags described below
  
- To run all the module from start to finish, execute the command `python3 CSEval.py -parse-and-all`
- Alternatively, if you have data in the same JSON format as the files within `./csnippex-apizator/input-posts` then the command `python3 CSEval.py -all` can be used

## CLI flags

This tool has CLI options as follows. One of them must be used when running the tool.

- `-parse-and-all` runs the entire process from `module A` to `module C`
  
  > i.e. All scripts below excluding `listgroups.py`
  
- `-all` runs `module B` and `module C`
  
  > i.e. All scripts below excluding `postpaser.py`, `deletednotrelatedposts.py` and `jsongenerator.py`
  
- `-parse-posts` executes the `postpaser.py` script
- `-filter-java` executes the `deletednotrelatedposts.py` script
- `-generate-json` executes the `jsongenerator.py` script
- `-csnippex-apizator` executes the `runtools.py` script
- `-group-answers` executes the `rename_and_group.py` script
- `-generate-run-tests` executes the `generateandrun.py` script
- `-analyse-answers` executes the `executiontime.py`, `executiontimeanalysis.py` and `staticanalysis.py` scripts
- `-generate-analysis` executes the `generateanalysis.py` script
- `-list-groups` executes the `listgroups.py` script
