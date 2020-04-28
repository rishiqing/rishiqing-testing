import os


def get_file_path(path):
    dir_path = os.path.split(os.path.abspath(__file__))[0]
    return dir_path[0:len(dir_path)-17] + path


def get_case_path(path):
    return get_file_path('/case/' + path)

