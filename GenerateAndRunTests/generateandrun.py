import os
import os.path
import subprocess
import json
import signal


def main():
    # compile the .java files and create tests
    arr = os.listdir('./output-rename')

    for file1 in arr:  # find classpath for file

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' +
                                 file1 + '/groups/' + file2)
                if len(arr) > 2:
                    for file3 in arr:

                        libs = ''
                        arr = os.listdir(
                            '../csnippex-apizator/output-apizator/')
                        for file4 in arr:

                            if file3 == file4.split('.', 1)[0]:
                                f = open(
                                    '../csnippex-apizator/output-apizator/' + file4, "r")
                                data = json.load(f)
                                libs = data['classPath']

                        try:

                            subprocess.run('javac ./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                           '/com/stackoverflow/api/SOClass.java', shell=True, check=True, timeout=10,
                                           capture_output=True)
                            p = subprocess.Popen(
                                ['java', '-classpath', '"./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                 '/:./randoop-all-4.3.0.jar:./maven-jars/jars/' + libs + '"', 'randoop.main.Main', 'gentests',
                                 '--testclass=com.stackoverflow.api.SOClass',
                                 '--junit-output-dir=./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                 '/com/stackoverflow/api/', '--regression-test-basename=Test' + file3,
                                 '--time-limit=15'],
                                shell=True, start_new_session=True)
                            p.wait(timeout=15)
                        except subprocess.CalledProcessError as e:
                            print(e)
                        except subprocess.TimeoutExpired:
                            print('timeout')
                            f.write('test timed out \n')
                            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                        except:
                            print("Something else went wrong")

    # run the tests and record results
    arr = os.listdir('./output-rename')

    for file1 in arr:

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                 '/groups/' + file2)

                if len(arr) > 2:
                    arr2 = os.listdir('./output-rename/' + file1 +
                                      '/groups/' + file2)

                    for file3 in arr:

                        arr = os.listdir('./output-rename/' + file1 +
                                         '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                        for file4 in arr:
                            if file4.startswith('Test') and file4.endswith('0.java'):

                                try:
                                    subprocess.run(
                                        'javac -cp "./junit-4.13.2.jar:./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                        '" ./output-rename/' + file1 +
                                        '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4,
                                        shell=True, check=True, timeout=10, capture_output=True)
                                    for placeholdername in arr2:
                                        print(placeholdername)

                                        f = open(
                                            './output-rename/' + file1 + '/groups/' + file2 + '/' + placeholdername +
                                            '/com/stackoverflow/api/' + placeholdername + 'TestResults.txt', "a")
                                        try:
                                            p = subprocess.Popen(['java', '-cp',
                                                                  './junit-4.13.2.jar:./hamcrest-core-1.3.jar'
                                                                  ':./output-rename/' + file1 + '/groups/' + file2 +
                                                                  '/' + file3 +
                                                                  '/com/stackoverflow/api:./output-rename/' + file1 +
                                                                  '/groups/' + file2 + '/' + placeholdername,
                                                                  'org.junit.runner.JUnitCore',
                                                                  file4.rsplit(".", 1)[0]],
                                                                 start_new_session=True, stdout=f, stderr=f)
                                            p.wait(timeout=15)
                                        except subprocess.CalledProcessError as e:
                                            print(e)
                                        except subprocess.TimeoutExpired:
                                            print('timeout')
                                            f.write('test timed out \n')
                                            os.killpg(os.getpgid(p.pid), signal.SIGTERM)

                                        f.close()

                                except:
                                    print("Something else went wrong")

    # run the tests and record results
    arr = os.listdir('./output-rename')

    for file1 in arr:

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                 '/groups/' + file2)

                if len(arr) > 2:

                    for file3 in arr:

                        arr = os.listdir('./output-rename/' + file1 +
                                         '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                        for file4 in arr:
                            if file4.startswith('SOClass') and file4.endswith('.java'):

                                try:
                                    print(file3)
                                    f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                             '/com/stackoverflow/api/' + file3 + 'StaticAnalysis.txt', "a")
                                    p = subprocess.Popen(['./bin/run.sh', 'pmd', '-d',
                                                          './output-rename/' + file1 + '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4,
                                                          '-R', 'rulesets/java/quickstart.xml', '-f', 'text'],
                                                         start_new_session=True)
                                    p.wait(timeout=15)

                                    f.close()

                                except subprocess.CalledProcessError as e:
                                    print(e)
                                except subprocess.TimeoutExpired:
                                    print('timeout')
                                    f.write('test timed out \n')
                                    os.killpg(os.getpgid(p.pid), signal.SIGTERM)


if __name__ == '__main__':
    main()
