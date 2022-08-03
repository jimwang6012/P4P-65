# CSnippEx and APIzator Tools for P4P 65

Valerio Terragni

## Requirements

- you should run the JARS with JDK 17
- the tools are tested in an Unix environment (Mac OSx, Linux, ...)

## content of the folder
- **csnippex.jar**
- **apizator.jar**	
- **csnippex.sh**	
- **apizator.sh**	
- **jdks** this folder contains some JDK for the compiler of CSnippEx, you should run CSnippEX with different JDK in input as some code snippets might compile only with some specific JDK version
- **input-posts**	- this folder should contain the posts in input in JSON format (one post in each file), CSnippEX will try to make them compilable. The posts has to be in the format of the SQL DB. 
- **output-csnippex** - Here there will be generated the compilable code snippets (if successful)
- **maven-jars** - This folder contains popular libraries, CsnippEx will try to compile the code snippets using the libraries. If libraries are needed in the classpath this will be included in the output JSON in `output-csnippex`
- **ser** - Some caching data, don't touch it. If you change the libraries in input just remove this folder, it will be created an updated one
- **output-apizator** - this folder will contain the output of APIzator.

## Instructions
- The input of APIzator is the output of CSnippEx
- Run `csnippex.sh` first, then `apizator.sh` then.
- I separate them as you need to analysed the compilable code snippets before the APIzation process
- If the tools are unsuccessful for a given code snippets no output will be generated, let me know if you prefer to get an error message of some type or log some information.