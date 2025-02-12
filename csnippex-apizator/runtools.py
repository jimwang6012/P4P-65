import json
import signal
import subprocess
import os
import os.path
import sys


def main():

    # run csnippex on input posts with 5 seconds timeout per post
    arr = os.listdir('input-posts')
    for file in arr:
        try:
            print('Processing ' + file)
            p = subprocess.Popen(['java', '-jar', 'csnippex.jar', './input-posts/' + file, './ser', './maven-jars', './jdks/jdk1.8.0_121.jdk', './tmp', './output-csnippex'],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' timed out')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished generating csnippex output')

    # run apizator on output of csnippex with 5 seconds timeout per post
    arr = os.listdir('output-csnippex')
    for file in arr:
        try:
            print('Processing ' + file)
            p = subprocess.Popen(['java', '-jar', 'apizator.jar', './output-csnippex/' + file, './output-apizator', './maven-jars'],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
            p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' timed out')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished generating apizator output')

    # convert the output of csnippex into java classes
    arr = os.listdir('output-csnippex')
    for file in arr:
        if file != "README.md":
            f = open("output-csnippex/" + file, "r")
            try:
                data = json.load(f)
            except UnicodeDecodeError:
                print("Cannot decode character - skipping")
            # create .java files in new directory
            os.makedirs('./output-csnippex-java', exist_ok=True)
            f = open('./output-csnippex-java/' +
                     str(data['postId']) + '.java', "w")
            f.write(
                data['body'])
            f.close()
    print('Finished converting csnippex output to java files')

    # convert the output of apizator into java classes
    arr = os.listdir('output-apizator')
    for file in arr:
        if file != "README.md":
            f = open("output-apizator/" + file, "r")
            data = json.load(f)
            # create .java files in new directory
            os.makedirs('./output-apizator-java', exist_ok=True)
            f = open('./output-apizator-java/' +
                     str(data['postId']) + '.java', "w")
            f.write(
                data['code'])
            f.close()
    print('Finished converting apizator output to java files')


if __name__ == '__main__':
    main()
