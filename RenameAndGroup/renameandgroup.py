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
            print('Renaming ' + file)
            post_id = file.split('.')[0]

            os.makedirs(f'../csnippex-apizator/output-rename/{str(dictionary[int(post_id)])}/{post_id}/com/stackoverflow/api', exist_ok=True)
            p = subprocess.Popen(['java', '-jar', 'rename-class.jar', '../csnippex-apizator/output-apizator-java/' + file,
                                  '../csnippex-apizator/output-csnippex-java/' + file, f'../csnippex-apizator/output-rename/{dictionary[post_id]}/{post_id}/com/stackoverflow/api/'], start_new_session=True)
            p.wait(timeout=5)
        except subprocess.CalledProcessError as e:
            print(e)
        except subprocess.TimeoutExpired:
            print(file + ' rename failed')
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    print('Finished renaming files')


if __name__ == '__main__':
    main()
