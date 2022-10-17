import os
import os.path
import subprocess
import json
import time
import signal

def main():

    arr = os.listdir('./output-rename')

    for file1 in arr:

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')

            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                '/groups/' + file2)

                if (len(arr) > 2):
                    arr2 = os.listdir('./output-rename/' + file1 +
                                    '/groups/' + file2)

                    for file3 in arr:
                       

                        f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                '/com/stackoverflow/api/' + file3 + 'ExecutionTime.txt', "w")
                        for x in range(10):
                            start_time = time.time()
                            for placeholdername in arr2:


                                arr = os.listdir('./output-rename/' + file1 +
                                                '/groups/' + file2 + '/' + placeholdername + '/com/stackoverflow/api')
                                for file4 in arr:

                                    if (file4 == 'Test' + placeholdername + '0.java'):

                                            try:
                                                p = subprocess.Popen(['java', '-cp', './junit-4.13.2.jar:./hamcrest-core-1.3.jar:./output-rename/' + file1 + '/groups/' + file2 + '/' + placeholdername + '/com/stackoverflow/api:./output-rename/' + file1 + '/groups/' + file2 + '/' + file3, 'org.junit.runner.JUnitCore', file4.rsplit(".", 1)[0]],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
                                                p.wait(timeout=15)
                                            except subprocess.CalledProcessError as e:
                                                print(e)
                                            except subprocess.TimeoutExpired:
                                                print('timeout')
                                                f.write('test timed out \n')
                                                os.killpg(os.getpgid(p.pid), signal.SIGTERM)




                            elapsed_time = time.time() - start_time
                            f.write(str(elapsed_time) + '\n')
                            print(elapsed_time)
                        f.close()


if __name__ == '__main__':
    main()