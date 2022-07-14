import sqlite3


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


def delete_questions_without_java_tag(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE PostTypeId = 1 AND Tags NOT LIKE '%<java>%'")


def delete_answers_without_code(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE PostTypeId = 2 AND Body NOT LIKE '%<pre><code>%'")


def delete_answers_not_related_to_java_questions(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE PostTypeId = 2 AND ParentId NOT IN (SELECT Id FROM posts WHERE PostTypeId = 1)")


def main():
    database = "../PostParser/so-posts.db"

    connection = create_connection(database)
    with connection:
        print("Deleting questions where Tags does not contain <java> ...")
        delete_questions_without_java_tag(connection)
        print("1/3 completed")

        print("Deleting answers where Body does not contain <pre> or <code> ...")
        delete_answers_without_code(connection)
        print("2/3 completed")

        print("Deleting answers not related to java questions ...")
        delete_answers_not_related_to_java_questions(connection)
        print("3/3 completed")


if __name__ == '__main__':
    main()
