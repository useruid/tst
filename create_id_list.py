import os


def get_filenames_from_directory(directory_path):
    """
    Reads all files from a directory and returns a list of filenames.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        list: A list containing the filenames in the directory.
    """
    try:
        # List all files and directories in the given path
        all_items = os.listdir(directory_path)

        # Filter out only files (excluding directories)
        filenames = [item for item in all_items if os.path.isfile(os.path.join(directory_path, item))]

        return filenames
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example usage
directory_path = "images/"
file_list = get_filenames_from_directory(directory_path)
print(file_list)