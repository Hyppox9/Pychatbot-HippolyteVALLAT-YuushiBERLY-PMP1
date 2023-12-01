import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)

mintxt = "haha"
print(mintxt)