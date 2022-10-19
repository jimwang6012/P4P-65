import sys
import os

from DeleteNotRelatedPosts import deletenotrelatedposts
from JSONGenerator import jsongenerator
from PostParser import postparser
from RenameAndGroup import rename_and_group
from GenerateAndRunTests import generateandrun, executiontime, executiontimeanalysis, staticanalysis, listgroups
from AnalyseResults import generateanalysis
from importlib.machinery import SourceFileLoader

csnippex_apizator = SourceFileLoader('csnippex_apizator', 'csnippex-apizator/runtools.py').load_module()


def main():
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the module to run')
        sys.exit()

    cwd = os.getcwd()

    flag = sys.argv[1]

    if flag == '-parse-posts' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./PostParser')
        postparser.main()

    if flag == '-filter-java' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./DeleteNotRelatedPosts')
        deletenotrelatedposts.main()

    if flag == '-generate-json' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./JSONGenerator')
        jsongenerator.main()

    if flag == '-csnippex-apizator' or flag == '-all' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./csnippex-apizator')
        csnippex_apizator.main()

    if flag == '-group-answers' or flag == '-all' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./RenameAndGroup')
        rename_and_group.main()

    if flag == '-generate-run-tests' or flag == '-all' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./GenerateAndRunTests')
        generateandrun.main()

    if flag == '-analyse-answers' or flag == '-all' or flag == '-parse-and-all':
        os.chdir(cwd)
        os.chdir('./GenerateAndRunTests')
        executiontime.main()
        executiontimeanalysis.main()
        staticanalysis.main()

    if flag == '-generate-analysis' or flag == '-all':
        os.chdir(cwd)
        os.chdir('./AnalyseResults')
        generateanalysis.main()

    if flag == '-list-groups':
        os.chdir(cwd)
        os.chdir('./GenerateAndRunTests')
        listgroups.main()

    else:
        print('Module not found')


if __name__ == '__main__':
    main()
