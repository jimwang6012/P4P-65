import subprocess


def main():
    subprocess.call(['java', '-jar', 'csnippex.jar', '../input-posts', './ser', './maven-jars', 'C:\Program Files\Java\jdk-17.0.2', './tmp', '../output-csnippex'])


if __name__ == '__main__':
    main()
