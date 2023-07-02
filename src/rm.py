import os
import shutil
import logging
import sys


def remove_directory(dir_path):
    try:
        os.rmdir(dir_path)
        logging.info(f"Removed directory: {dir_path}")
    except FileNotFoundError:
        logging.error(f"Directory not found: {dir_path}")
    except PermissionError:
        logging.error(f"Permission denied: {dir_path}")
    except OSError:
        logging.error(f"Directory not empty: {dir_path}")
    except Exception as e:
        logging.error(f"Error occurred while deleting directory: {e}")


def remove_file(file_path):
    try:
        os.remove(file_path)
        logging.info(f"Removed file: {file_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while deleting file: {e}")


def remove_directory_recursive(dir_path):
    try:
        shutil.rmtree(dir_path)
        logging.info(f"Removed directory: {dir_path}")
    except FileNotFoundError:
        logging.error(f"Directory not found: {dir_path}")
    except PermissionError:
        logging.error(f"Permission denied: {dir_path}")
    except Exception as e:
        logging.error(f"Error occurred while deleting directory: {e}")


def confirm_content_delete(path):
    return input(f"Sure you want to delete the directory with the path \"{path}\" and it's "
                 f"contents (Y/n): ")


class RmCmd:
    def __init__(self, args):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        self.recursive = args.recursive
        self.force = args.force
        self.paths = args.paths
        self.handle_command()

    def check_content_deletion(self, path):
        delete = True
        if not self.force:
            counter = 1
            ans = confirm_content_delete(path)
            while (ans != "Y" and ans != "n" and ans != "N") and counter < 2:
                ans = confirm_content_delete(path)
                counter += 1

            if ans != "Y" and ans != "y":
                delete = False
                logging.warning("Cancel operation.")

        return delete

    def handle_command(self):
        for path in self.paths:
            if os.path.isfile(path):
                remove_file(path)
            elif os.path.isdir(path):
                if self.recursive:
                    delete = self.check_content_deletion(path)
                    remove_directory_recursive(path) if delete else None
                else:
                    remove_directory(path)
            else:
                logging.warning(f"Invalid path: {path}")
