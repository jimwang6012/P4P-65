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


def select_posts_with_java_tag(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts WHERE Tags LIKE '<java>' LIMIT 100")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def main():
    database = "../PostParser/so-posts.db"

    connection = create_connection(database)
    with connection:
        print("1. Tags contains <java> Query")
        select_posts_with_java_tag(connection)


if __name__ == '__main__':
    main()
