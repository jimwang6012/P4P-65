from datetime import timedelta
import os

def main():
    arr = os.listdir('./output-rename')

    for file1 in arr:

        if file1 != "README.md":
            arr = os.listdir('./output-rename/' + file1 + '/groups')
          
            for file2 in arr:

                arr = os.listdir('./output-rename/' + file1 +
                                '/groups/' + file2)

                if (len(arr) > 2):
          

                    for file3 in arr:
            
                        arr = os.listdir('./output-rename/' + file1 +
                                        '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                        for file4 in arr:

                            if (file4 == file3 + 'ExecutionTime.txt'):
                                print(file4)
                               
                                # Using readlines()
                                execution_file = open('./output-rename/' + file1 +
                                        '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4, 'r')
                                Lines = execution_file.readlines()
                                
                                count = 0
                                sum = 0
                                max = 0
                                min = 200
                                timed_out = False
                                # Strips the newline character
                                for line in Lines:
                                    print(line.strip())
                                    if (line.strip() == 'test timed out'):
                                        timed_out = True
                                        break    
                                    
                                    if (float(line.strip()) > max):
                                        max = float(line.strip())
                                        
                                    if (float(line.strip()) < min):
                                        min = float(line.strip())
                                        
                                    sum += float(line.strip())
                                    
                                f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file3 +
                                    '/com/stackoverflow/api/' + file3 + 'ExecutionTimeAnalysis.txt', "w")
                                if timed_out == False:    
                                    avg = sum/10
                                    
                                    f.write(str(avg) + '\n')
                                    f.write(str(max) + '\n')
                                    f.write(str(min) + '\n')
                                    
                                else:
                                    f.write('test timed out')
                                
                                f.close()
                                execution_file.close()
                                
    arr1 = os.listdir('./output-rename')

    for file1 in arr1:

        if file1 != "README.md":
            arr2 = os.listdir('./output-rename/' + file1 + '/groups')
          
            for file2 in arr2:
                
                # if os.path.exists('./output-rename/' + file1 + '/groups/' + file2 + '/' + file1 + file2 + 'GroupExecutionTimeAnalysis.txt'):
                #     os.remove('./output-rename/' + file1 + '/groups/' + file2 + '/' + file1 + file2 + 'GroupExecutionTimeAnalysis.txt')
                # else:
                #     print("The file does not exist")
                
                # if os.path.exists('./output-rename/' + file1 + '/groups/' + file2 + 'GroupExecutionTimeAnalysis.txt'):
                #     os.remove('./output-rename/' + file1 + '/groups/' + file2 + 'GroupExecutionTimeAnalysis.txt')
                # else:
                #     print("The file does not exist")

                arr3 = os.listdir('./output-rename/' + file1 +
                                '/groups/' + file2)

                if (len(arr3) > 2):
                    
                    count = 0
                    sum = 0
                    max = 0
                    min = 200
                    
                    f = open('./output-rename/' + file1 + '/groups/' + file2 + '/' + file1 + '_' + file2 + '_' + 'ExecutionTimeAnalysis.txt', "w")
                        

                    
                    for file3 in arr3:
                        if (file3 != file1 + '_' + file2 + '_' + 'ExecutionTimeAnalysis.txt'):
                            arr4 = os.listdir('./output-rename/' + file1 +
                                            '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api')
                            for file4 in arr4:

                                if (file4 == file3 + 'ExecutionTimeAnalysis.txt'):
                                    print(file4)
                                
                                    # Using readlines()
                                    execution_file = open('./output-rename/' + file1 +
                                            '/groups/' + file2 + '/' + file3 + '/com/stackoverflow/api/' + file4, 'r')
                                    Lines = execution_file.readlines()
                                    timed_out = False
                                    if (Lines[0] == 'test timed out'):
                                        timed_out = True
                                        print(Lines[0].strip())
                                    else:
                                        print(Lines[0].strip())
                                        sum += float(Lines[0].strip())
                                        count += 1
                                        print(Lines[1].strip())
                                        if (float(Lines[1].strip()) > max):
                                            max = float(Lines[1].strip())
                                        print(Lines[2].strip())
                                        if (float(Lines[2].strip()) < min):
                                            min = float(Lines[2].strip())
                                    
                        
                                    execution_file.close()
                                    
                    if (count > 0):
                        print ('avg is ' + str(sum/count))
                        f.write(str(sum/count) + '\n')
                        print('max is ' + str(max))
                        f.write(str(max) + '\n')
                        print('min is ' + str(min))
                        f.write(str(min) + '\n')
                    else:
                        print('all tests timed out')
                        f.write('test timed out')
                    
                    f.close()
                    
    arr1 = os.listdir('./output-rename')
    count = 0
    sum = 0
    max = 0
    min = 200
    f = open('./output-rename/' + 'OverallExecutionTimeAnalysis.txt', "w")
    for file1 in arr1:

        if file1 != "README.md" and file1 != 'OverallExecutionTimeAnalysis.txt':
            arr2 = os.listdir('./output-rename/' + file1 + '/groups')
          
            for file2 in arr2:


                arr3 = os.listdir('./output-rename/' + file1 +
                                '/groups/' + file2)

                if (len(arr3) > 2):
                    
                    for file3 in arr3:
                        if (file3 == file1 + '_' + file2 + '_' + 'ExecutionTimeAnalysis.txt'):
                            print(file3)
                            execution_file = open('./output-rename/' + file1 +
                                    '/groups/' + file2 + '/' + file3, 'r')
                            Lines = execution_file.readlines()
                            timed_out = False
                            if (Lines[0] == 'test timed out'):
                                timed_out = True
                                print(Lines[0].strip())
                            else:
                                print(Lines[0].strip())
                                sum += float(Lines[0].strip())
                                count += 1
                                print(Lines[1].strip())
                                if (float(Lines[1].strip()) > max):
                                    max = float(Lines[1].strip())
                                    
                                    
                                if (float(Lines[2].strip()) < min):
                                    min = float(Lines[2].strip())
                                    
                        
                            execution_file.close()

    if (count > 0):
        print ('avg is ' + str(sum/count))
        f.write(str(sum/count) + '\n')
        print('max is ' + str(max))
        f.write(str(max) + '\n')
        print('min is ' + str(min))
        f.write(str(min) + '\n')
    else:
        print('all tests timed out')
        f.write('test timed out')
    f.close()
    
if __name__ == '__main__':
    main()