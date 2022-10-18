import os
import os.path
from tabulate import tabulate


def main():
    # compile the .java files and create tests
    arr = os.listdir('../GenerateAndRunTests/output-rename')

    for file1 in arr:  # find classpath for file

        if file1 != "README.md":
            arr = os.listdir('../GenerateAndRunTests/output-rename/' + file1 + '/groups')
            for file2 in arr:

                arr = os.listdir('../GenerateAndRunTests/output-rename/' +
                                 file1 + '/groups/' + file2)
                if len(arr) > 2:
                    title = "Post " + file1 + " | " + file2
                    header = ["Answers"]
                    test_order = []
                    results_dict = {}
                    for temp_file in arr:
                        results_dict[temp_file] = []
                    for file3 in arr:
                        if file3 != "CorrectnessTable.txt":
                            temp_test_order = []
                            test_count = 0
                            results = []
                            try:
                                with open('../GenerateAndRunTests/output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                      '/com/stackoverflow/api/' + file3 + 'TestResults.txt', 'r') as f:
                                    skip = False
                                    for line in f.readlines():
                                        if line.startswith('Test') and line.endswith('0.java\n'):
                                            temp_test_order.append(line.split('Test')[1].split('0.java\n')[0])
                                        if line.startswith('Test' + file3 + '0.java'):
                                            skip = True
                                            results.append("-")
                                            continue
                                        if skip:
                                            if line.startswith('Test') and line.endswith('0.java\n'):
                                                skip = False
                                                continue
                                            else:
                                                continue
                                        if line.startswith('OK ('):
                                            passed = int(line.split('OK (')[1].split(' test')[0])
                                            test_count += passed
                                            results.append(f"P:{str(passed)} F:0 100%")
                                        if line.startswith('Tests run:'):
                                            line_data = line.split('Tests run: ')[1].split(',  Failures: ')
                                            passed = int(line_data[0])
                                            failed = int(line_data[1])
                                            confidence = passed / (passed + failed) * 100
                                            test_count += passed
                                            test_count += failed
                                            results.append(f"P:{str(passed)} F:{str(failed)} {str(round(confidence, 2))}%")
                            except FileNotFoundError as e:
                                print(e)
                            if len(temp_test_order) > len(test_order):
                                test_order = temp_test_order
                            if test_count != 0:
                                results_dict[file3] = results

                    is_empty = True
                    for v in results_dict.values():
                        if len(v) != 0:
                            is_empty = False

                    if not is_empty:
                        header += test_order
                        table_results = []
                        for test_id in test_order:
                            if len(results_dict[test_id]) != 0:
                                table_results.append([test_id] + results_dict[test_id])

                        print(title)
                        print(tabulate(table_results, headers=header, tablefmt="fancy_grid"))

                    with open('../GenerateAndRunTests/output-rename/' +
                                 file1 + '/groups/' + file2 + '/CorrectnessTable.txt', 'w') as outfile:
                        outfile.writelines([title + '\n', tabulate(table_results, headers=header, tablefmt="grid")])

if __name__ == '__main__':
    main()
