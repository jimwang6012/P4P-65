import os
import os.path
from tabulate import tabulate
import numpy as np


def average(arr):
    return sum(arr) / len(arr)


def inter_quartile_range(arr):
    data = np.array(arr)
    q3, q1 = np.percentile(data, [75, 25])
    iqr = q3 - q1
    return q1, q3, iqr


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
                    confidence_dict = {}
                    exec_time_dict = {}
                    warning_count_dict = {}
                    correctness_outliers = []
                    exec_time_outliers = []
                    for temp_file in arr:
                        if temp_file != "AnalysisTable.txt":
                            results_dict[temp_file] = []
                            confidence_dict[temp_file] = 0.0
                            exec_time_dict[temp_file] = 0.0
                            warning_count_dict[temp_file] = 0
                    for file3 in arr:
                        if file3 != "AnalysisTable.txt":
                            temp_test_order = []
                            test_count = 0
                            results = []
                            confidence_list = []
                            avg_exec_time = None
                            warning_count = 0
                            try:
                                with open(
                                        '../GenerateAndRunTests/output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                        '/com/stackoverflow/api/' + file3 + 'ExecutionTimeAnalysis.txt', 'r') as f:
                                    first_line = f.readline()
                                    if first_line != "test timed out":
                                        avg_exec_time = round(float(f.readline()), 2)
                            except FileNotFoundError as e:
                                print(e)

                            try:
                                with open(
                                        '../GenerateAndRunTests/output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                        '/com/stackoverflow/api/' + file3 + 'StaticAnalysisParsing.txt', 'r') as f:
                                    warning_count = int(f.readline())
                            except FileNotFoundError as e:
                                print(e)

                            try:
                                with open(
                                        '../GenerateAndRunTests/output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
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
                                            confidence_list.append(100.0)
                                        if line.startswith('Tests run:'):
                                            line_data = line.split('Tests run: ')[1].split(',  Failures: ')
                                            passed = int(line_data[0])
                                            failed = int(line_data[1])
                                            confidence = passed / (passed + failed) * 100
                                            test_count += passed
                                            test_count += failed
                                            results.append(
                                                f"P:{str(passed)} F:{str(failed)} {str(round(confidence, 2))}%")
                                            confidence_list.append(confidence)
                            except FileNotFoundError as e:
                                print(e)
                            if len(temp_test_order) > len(test_order):
                                test_order = temp_test_order
                            if test_count != 0:
                                results_dict[file3] = results
                                confidence_dict[file3] = round(average(confidence_list), 2)
                                exec_time_dict[file3] = avg_exec_time
                                warning_count_dict[file3] = warning_count

                    is_empty = True
                    for v in results_dict.values():
                        if len(v) != 0:
                            is_empty = False

                    if not is_empty:
                        correctness_group = []
                        exec_time_group = []
                        for test_id in test_order:
                            correctness_group.append(confidence_dict[test_id])
                            exec_time_group.append(exec_time_dict[test_id])
                        correctness_q1, correctness_q3, correctness_iqr = inter_quartile_range(correctness_group)
                        exec_time_q1, exec_time_q3, exec_time_iqr = inter_quartile_range(exec_time_group)

                        header += test_order
                        header.append("AVG Correctness")
                        header.append("AVG Execution Time")
                        header.append("PMD Violations")
                        table_results = []
                        for test_id in test_order:
                            if len(results_dict[test_id]) != 0:

                                if confidence_dict[test_id] < (correctness_q1 - 1.5 * correctness_iqr):
                                    correctness_outliers.append(test_id)
                                if exec_time_dict[test_id] > (exec_time_q3 + 1.5 * exec_time_iqr):
                                    exec_time_outliers.append(test_id)

                                table_results.append([test_id] + results_dict[test_id] +
                                                     [str(confidence_dict[test_id]) + "%"] +
                                                     [exec_time_dict[test_id]] + [warning_count_dict[test_id]])

                        with open('../GenerateAndRunTests/output-rename/' +
                                  file1 + '/groups/' + file2 + '/AnalysisTable.txt', 'w') as outfile:

                            print(title)
                            print(tabulate(table_results, headers=header, tablefmt="fancy_grid"))

                            if len(correctness_outliers) == 0:
                                correctness_outliers_string = "Correctness Outliers: None"
                            else:
                                correctness_outliers_string = "Correctness Outliers: " + ", ".join(correctness_outliers)
                            if len(exec_time_outliers) == 0:
                                exec_time_outliers_string = "Execution Time Outliers: None"
                            else:
                                exec_time_outliers_string = "Execution Time Outliers: " + ", ".join(exec_time_outliers)

                            print(correctness_outliers_string)
                            print(exec_time_outliers_string)
                            print()

                            outfile.writelines([title + '\n', tabulate(table_results, headers=header, tablefmt="grid"),
                                                '\n' + correctness_outliers_string, '\n' + exec_time_outliers_string, '\n'])


if __name__ == '__main__':
    main()
