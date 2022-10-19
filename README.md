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

- Install Python 3.x from [here](https://www.python.org/downloads/).

- Install JDK 18 from [here](https://www.oracle.com/java/technologies/javase/jdk18-archive-downloads.html).
  
## Required Modules

Numerous Python modules will need to be installed to run the tool. 

- Install the modules by executing `pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`

## Running the tool

In order to run the tool, follow these steps

- Open your terminal and set the working directory to ./GenerateAndRunTests.
- Execute the commands `chmod u+r+x ./bin/pmd.bat` and `chmod u+r+x ./bin/run.sh` in the terminal to give access permission to the static analysis tools.
- Set the working directory back to ./P4P-65
- Execute the CLI command `...` with set flags

## CLI Options

This tool has CLI options as follows

- `-parse-and-all` runs the entire process from `module A` to `module C`
- `-all` runs `module B` and `module C`
- `-parse-posts` executes the `postpaser.py` script
- `-filter-java` executes the `deletednotrelatedposts.py` script
- `-generate-json` executes the `jsongenerator.py` script
- `-csnippex-apizator` executes the `runtools.py` script
- `-group-answers` executes the `rename_and_group.py` script
- `-generate-run-tests` executes the `generateandrun.py` script
- `-analyse-answers` executes the `executiontime.py`, `executiontimeanalysis.py` and `staticanalysis.py` scripts
- `-generate-analysis` executes the `generateanalysis.py` script
- `-list-groups` executes the `listgroups.py` script



