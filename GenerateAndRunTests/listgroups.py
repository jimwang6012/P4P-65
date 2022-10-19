import os


def main():
    # list all groups
    arr = os.listdir('./output-rename')

    for file1 in arr:

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                 '/groups/' + file2)

                if len(arr) > 2:
                    print('./output-rename/' + file1 +
                          '/groups/' + file2)


if __name__ == '__main__':
    main()
