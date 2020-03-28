import os
import time
import logging

module_logger = logging.getLogger("reports_application")


def init_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def write_userinfo(user_info, directory, filename):
    filepath = directory + '/' + filename
    file_extension = '.txt'
    if os.path.isfile(filepath):
        file_mod_time = time.localtime(os.path.getmtime(filepath))
        os.replace(filepath, filepath + '_' + time.strftime("%Y-%m-%dT%H:%M", file_mod_time) + file_extension)
    try:
        with open(filepath, 'w') as file_handler:
            file_handler.write(user_info)
    except IOError:
        module_logger.error("Error while saving report at filepath: " + filepath)
    finally:
        print('finally')
