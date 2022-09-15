import os

dir_path = "F:\SELENIUM_PROJECTS\CSV_FILE_TO_ORACLE_DB_BY_PYTHON"     # mention path here like F:\PROJECTS\folder_name

def delete_all_file(dir_path):
    dir_list = os.listdir(dir_path)
    for item in dir_list:
        if item.endswith(".csv"):
            path = os.path.join(dir_path, item)
            print(path)
            os.remove(path)

delete_all_file(dir_path)