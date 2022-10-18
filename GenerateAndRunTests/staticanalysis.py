import os

def main():
    arr1 = os.listdir('./output-rename')
 
    for file1 in arr1:

        if file1 != "README.md" and file1 != 'OverallExecutionTimeAnalysis.txt':
            arr2 = os.listdir('./output-rename/' + file1 + '/groups')
          
            for file2 in arr2:

         
                arr3 = os.listdir('./output-rename/' + file1 +
                                    '/groups/' + file2)
                if (len(arr3) > 2):
                    
                    for file3 in arr3:
                        if (file3 != file1 + '_' + file2 + '_' + 'StaticAnalysisParsing.txt' and file3 != file1 + '_' + file2 + '_' + 'ExecutionTimeAnalysis.txt'):
                        
                            arr4 = os.listdir('./output-rename/' + file1 +
                                            '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                            for file4 in arr4:

                                if (file4 == file3 + 'StaticAnalysis.txt'):
                                    count = 0
                                    sum = 0
                                    max = 0
                                    min = 200
                                    print(file4)
                                    execution_file = open('./output-rename/' + file1 +
                                    '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4, 'r')
                                    Lines = execution_file.readlines()
                                    for line in Lines:
                                        if(line.strip().startswith('C:')):
                                            sum += 1
                                            
                                    f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                    '/com/stackoverflow/api/' + file3 + 'StaticAnalysisParsing.txt', "w")
                                    
                                    print(sum)
                                    f.write(str(sum))
                                    f.close()
                                    execution_file.close()      


if __name__ == '__main__':
    main()