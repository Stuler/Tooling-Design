import os


def get_folder():
    path = input("Path to directory: ")
    return path


def get_files_list(path):
    opt = 1
    for i in os.listdir(path):
        print(f"{opt} - {i}")
        opt += 1


def get_folder_structure(path):
    folder_lst = []
    for i in os.listdir(path):
        folder_lst.append(i)
    for n in range(len(folder_lst)):
        folder_structure = {
            n+1: folder_lst[n] for n in range(len(folder_lst))
        }
    for key, value in folder_structure.items():
        print(f"{key}   -   {value}")
    return(folder_structure)
