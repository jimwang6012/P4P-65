import signal
import subprocess
import os
import os.path


def main():

    # run rename-class on apizator output .java files with 5 seconds timeout
    arr = os.listdir('../csnippex-apizator/output-apizator-java')
    num = 0
    for file in arr:
        num += 1
        try:
            print('Renaming ' + file)
            os.makedirs('../csnippex-apizator/hi/' + str(num), exist_ok=True)
            p = subprocess.Popen(['java', '-jar', 'rename-class.jar', '../csnippex-apizator/output-apizator-java/' + file,
                                  '../csnippex-apizator/output-csnippex-java/' + file, '../csnippex-apizator/hi/' + str(num) + '/'], start_new_session=True)
            p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' rename failed')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished renaming files')


if __name__ == '__main__':
    main()
