import subprocess
import os
import os.path
from subprocess import Popen, PIPE
import sys
import json


def main():

    # run csnippex on input posts with 10 seconds timeout per post
    arr = os.listdir('input-posts')
    for file in arr:
        try:
            print('processing ' + file)
            subprocess.run('java -jar csnippex.jar ./input-posts/' + file +
                           ' ./ser ./maven-jars ./jdks/jdk-17.0.2.jdk ./tmp ./output-csnippex', shell=True, check=True, timeout=10, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' timed out')
    print('finished generating csnippex output')

    # run apizator on output of csnippex with 10 seconds timeout per post
    arr = os.listdir('output-csnippex')
    for file in arr:
        try:
            print('processing ' + file)
            subprocess.run('java -jar apizator.jar ./output-csnippex/' + file +
                           ' ./output-apizator ./maven-jars', shell=True, check=True, timeout=10, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' timed out')
    print('finished generating apizator output')

    # convert the output of apizator into java classes and then compile the classes
    arr = os.listdir('output-apizator')
    for file in arr:
        f = open("output-apizator/" + file, "r")
        data = json.load(f)
        # create .java files in new directory
        os.makedirs('./com/stackoverflow/api', exist_ok=True)
        f = open('./com/stackoverflow/api/' +
                 data['className'] + '.java', "w")
        f.write(
            data['code'])
        f.close()
        try:
            # compile the .java files
            subprocess.run("javac ./com/stackoverflow/api/" +
                           data['className'] + '.java', shell=True, check=True, timeout=10, capture_output=True)
            # store the compiled classes to be tested
            f = open('classlist.txt', "a")
            f.write('com.stackoverflow.api.' + data['className'] + '\n')
            f.close()
            print('compiled ' + data['className'])
        except subprocess.CalledProcessError as e:
            print(e)
    print('finished compiling java files')

    # create directory to store generated tests
    os.makedirs('./test', exist_ok=True)
    # run randoop on the generated class files
    subprocess.call(
        'java -classpath "./:randoop-all-4.3.0.jar" randoop.main.Main gentests --classlist="classlist.txt" --junit-output-dir="./test" --time-limit=30', shell=True)
    print('finished generating randoop tests')

    sys.exit()


if __name__ == '__main__':
    main()
