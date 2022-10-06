import os
import os.path
import subprocess
import json


def main():

    # compile the .java files and create tests
    arr = os.listdir('./output-rename')
    count1 = 0
    for file1 in arr: # find classpath for file
        count1+=1
        if (count1 < 3):
            # print (file1)
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:
                # print(file2)
                arr = os.listdir('./output-rename/' + file1 + '/groups/' + file2)
                if (len(arr) > 2):
                    for file3 in arr:
                        # print(file3)
                        libs = ''
                        arr = os.listdir('../csnippex-apizator/output-apizator/')
                        for file4 in arr:

                            if (file3 == file4.split('.', 1)[0]):

                                f = open('../csnippex-apizator/output-apizator/' + file4, "r")
                                data = json.load(f)
                                libs = data['classPath']

                        # print(libs)

                        try:

                            subprocess.run('javac ./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                        '/com/stackoverflow/api/SOClass.java', shell=True, check=True, timeout=10, capture_output=True)
                            subprocess.call(
                                'java -classpath "./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                '/:./randoop-all-4.3.0.jar:./maven-jars/jars/' + libs + '" randoop.main.Main gentests --testclass="com.stackoverflow.api.SOClass"  --junit-output-dir="./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                '/com/stackoverflow/api/" --regression-test-basename=Test' + file3 + ' --time-limit=30', shell=True)

                    # subprocess.run('java -jar evosuite-1.0.6.jar -class com.stackoverflow.api.SOClass -projectCP ./output-runtools/' + file1 + '/' + file2 +
                    #                '/', shell=True, check=True, timeout=10, capture_output=True)
                        except subprocess.CalledProcessError as e:
                            print(e)
                        except:
                            print("Something else went wrong")

    # run the tests and record results
    arr = os.listdir('./output-rename')
    count2 = 0
    for file1 in arr:
        count2+=1
        if (count2 < 3):
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                 '/groups/' + file2)

                if (len(arr) > 2):
                    arr2 = os.listdir('./output-rename/' + file1 +
                                      '/groups/' + file2)

                    for file3 in arr:

                        arr = os.listdir('./output-rename/' + file1 +
                                         '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                        for file4 in arr:
                            if (file4.startswith('Test') and file4.endswith('0.java')):

                                try:
                                    subprocess.run('javac -cp "./junit-4.13.2.jar:./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                                   '" ./output-rename/' + file1 +
                                                   '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4, shell=True, check=True, timeout=10, capture_output=True)
                                    for placeholdername in arr2:
                                        print(placeholdername)

                                        f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + placeholdername +
                                                 '/com/stackoverflow/api/' + placeholdername + 'TestResults.txt', "a")
                                        with subprocess.Popen('java -cp "./junit-4.13.2.jar:./hamcrest-core-1.3.jar:./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api:./output-rename/' + file1 + '/groups/' + file2 + '/' + placeholdername +
                                                              '" org.junit.runner.JUnitCore ' + file4.rsplit(".", 1)[0], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
                                            f.write(file4 + '\n')
                                            for line in process.stdout:
                                                print(line.decode('utf8'))
                                                f.write(line.decode(
                                                        'utf8') + '\n')

                                        f.close()

                                except:
                                    print("Something else went wrong")

    # run the tests and record results
    arr = os.listdir('./output-rename')
    count3 = 0
    for file1 in arr:
        count3+=1
        if (count3 < 3):
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                 '/groups/' + file2)

                if (len(arr) > 2):
                    arr2 = os.listdir('./output-rename/' + file1 +
                                      '/groups/' + file2)

                    for file3 in arr:

                        arr = os.listdir('./output-rename/' + file1 +
                                         '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                        for file4 in arr:
                            if (file4.startswith('SOClass') and file4.endswith('.java')):

                                try:
                                    f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                             '/com/stackoverflow/api/' + file3 + 'StaticAnalysis.txt', "a")
                                    with subprocess.Popen(r'.\bin\pmd.bat -d ./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4 + 
                                                          ' -f text -R rulesets/java/quickstart.xml', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
                                        f.write(file3 + '\n')
                                        for line in process.stdout:
                                            print(line.decode('utf8'))
                                            f.write(line.decode(
                                                'utf8') + '\n')

                                    f.close()

                                except:
                                    print("Something else went wrong")



if __name__ == '__main__':
    main()
