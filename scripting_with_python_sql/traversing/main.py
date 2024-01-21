import os


def main():
    for root, directories, files in os.walk("/home/dcti-02-11/projects/data"):
        # print(f"Root {root}")
        # print(f" {directories}")
        # print(f" {files}")
        for _file in files:
            absolute_path = os.path.join(root, _file)
            print(f"File path : {absolute_path}")


if __name__ == '__main__':
    main()
