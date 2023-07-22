import argparse
from src.rm import RmCmd

def main():
    parser = argparse.ArgumentParser(description="Delete files/directories with options.")
    parser.add_argument("paths", help="Path of the file or directory to delete.", nargs="*", default=[])
    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Remove directories and their contents recursively.")
    parser.add_argument("-f", "--force", action="store_true", help="Force deletion without prompting for confirmation.")
    args = parser.parse_args()

    try:
        RmCmd(args)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by the user")


if __name__ == "__main__":
    main()