import os


def main():
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

                            if file4 == file3 + 'ExecutionTime.txt':
                                print(file4)

                                # Using readlines()
                                execution_file = open('./output-rename/' + file1 +
                                                      '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4,
                                                      'r')
                                lines = execution_file.readlines()

                                count = 0
                                sum = 0
                                max = 0
                                min = 200
                                timed_out = False
                                # Strips the newline character
                                for line in lines:
                                    print(line.strip())
                                    if line.strip() == 'test timed out':
                                        timed_out = True
                                        break

                                    if float(line.strip()) > max:
                                        max = float(line.strip())

                                    if float(line.strip()) < min:
                                        min = float(line.strip())

                                    sum += float(line.strip())

                                f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                         '/com/stackoverflow/api/' + file3 + 'ExecutionTimeAnalysis.txt', "w")
                                if not timed_out:
                                    avg = sum / 10

                                    f.write(str(avg) + '\n')
                                    f.write(str(max) + '\n')
                                    f.write(str(min) + '\n')

                                else:
                                    f.write('test timed out')

                                f.close()
                                execution_file.close()


if __name__ == '__main__':
    main()
