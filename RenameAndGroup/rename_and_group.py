import shutil
import signal
import sqlite3
import subprocess
import os
import os.path


def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return connection


def main():

    # dictionary to store each postId with parentId
    # dictionary[postId] = parentId
    dictionary = {}
    database = "../csnippex-apizator/id-matching.db"
    connection = create_connection(database)

    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM post_ids")
        for row in cursor:
            dictionary[row[0]] = row[1]

    # run rename-class on apizator output .java files with 5 seconds timeout
    arr = os.listdir('../csnippex-apizator/output-apizator-java')
    for file in arr:
        try:
            if file != "README.md":
                print('Renaming ' + file)
                post_id = file.split('.')[0]

                os.makedirs(
                    f'../GenerateAndRunTests/output-rename/{str(dictionary[int(post_id)])}/{post_id}/com/stackoverflow/api', exist_ok=True)
                p = subprocess.Popen(['java', '-jar', 'rename-class.jar', '../csnippex-apizator/output-apizator-java/' + file,
                                      '../csnippex-apizator/output-csnippex-java/' + file, f'../GenerateAndRunTests/output-rename/{str(dictionary[int(post_id)])}/{post_id}/com/stackoverflow/api/'], start_new_session=True)
                p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' rename failed')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished renaming files')

    # purge empty answers
    arr = os.listdir('../GenerateAndRunTests/output-rename')
    for file in arr:
        try:
            if file != "README.md":
                path = '../GenerateAndRunTests/output-rename/' + file
                answers = os.listdir(path)
                for answer in answers:
                    if answer != "groups":
                        if not os.path.exists(path + "/" + answer + "/com/stackoverflow/api/SOClass.java"):
                            print("Removing empty answer " + answer + " from " + file)
                            shutil.rmtree(path + "/" + answer)
        except OSError as e:
            print(e)
    print('Finished purging empty answers')

    # run group-class on output-rename files with 5 seconds timeout
    arr = os.listdir('../GenerateAndRunTests/output-rename')
    for file in arr:
        try:
            if file != "README.md":
                print('Grouping answers in ' + file)

                p = subprocess.Popen(['java', '-jar', 'group-class.jar', '../GenerateAndRunTests/output-rename/' + file], start_new_session=True)
                p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' grouping failed')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished grouping answers')


if __name__ == '__main__':
    main()
