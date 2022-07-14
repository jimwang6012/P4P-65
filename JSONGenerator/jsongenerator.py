import sqlite3
import json
from datetime import datetime


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


def select_posts_with_more_than_20_answers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT table1.* FROM posts AS table1 JOIN (SELECT ParentId FROM posts WHERE ParentId IN "
                   "(SELECT Id FROM posts WHERE PostTypeId = 1) GROUP BY ParentId HAVING COUNT(ParentId) >= 20) "
                   "AS table2 ON table1.ParentId = table2.ParentId")

    count = 0

    for row in cursor:
        path_string = "../input-posts/" + str(row[2]) + "-" + str(row[0]) + ".json"
        data = {
            "Id":row[0],
            "PostTypeId":row[1],
            "AcceptedAnswerId":row[3],
            "ParentId":row[2],
            "Score":row[5],
            "ViewCount":row[6],
            "Body":row[7].replace("\n", " "),
            "OwnerUserId":row[8],
            "LastEditorUserId":row[10],
            "LastActivityDate":datetime.strftime(datetime.fromisoformat(row[13]), "%b %d, %Y"),
            "AnswerCount":row[17],
            "CommentCount":row[18],
            "FavoriteCount":row[19],
            "CreationDate":datetime.strftime(datetime.fromisoformat(row[4]), "%b %d, %Y")
        }

        with open(path_string, 'w') as file:
            json.dump(data, file)

        count += 1

    print("Created " + str(count) + " JSON files")


def main():
    database = "../PostParser/so-posts.db"

    connection = create_connection(database)
    with connection:
        print("Creating JSONs from posts with more than 20 answers ...")
        select_posts_with_more_than_20_answers(connection)


if __name__ == '__main__':
    main()
