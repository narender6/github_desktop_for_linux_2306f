import sys

def run(*args):
    return 'Hello from Github Desktop For Linux (built from demand: https://github.com/desktop/desktop/issues/1525)'

def cli(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    print(run(*argv)); return 0

if __name__ == '__main__':
    sys.exit(cli())
