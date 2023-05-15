import argparse
import os
from collections import ChainMap

def main():
    app_default = {"username": "admin", "password": "admin"}

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ, app_default)
    print(chain["username"])


if __name__ == "__main__":
    main()
    os.environ["username"] = "test"
    main()