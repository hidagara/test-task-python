import os
import time
import logging

module_logger = logging.getLogger("reports_application")


def init_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def create_timestamp_file(directory, filename, file_extension, timestamp):
    filepath = directory + '/' + filename
    if os.path.isfile(filepath):
        os.replace(filepath, filepath + '_' + timestamp + file_extension)


def restore_file_from_timestamp(directory, filename, file_extension, timestamp):
    filepath = directory + '/' + filename
    timestamp_filepath = filepath + '_' + timestamp + file_extension
    if os.path.isfile(filepath):
        print("restore file at " + timestamp_filepath)
        os.replace(timestamp_filepath, filepath + '.txt')


def write_userinfo(user_info, directory, filename):
    filepath = directory + '/' + filename
    file_extension = '.txt'

    try:
        if os.path.isfile(filepath):
            file_mod_time = time.localtime(os.path.getmtime(filepath))
            timestamp = time.strftime("%Y-%m-%dT%H:%M", file_mod_time)
            create_timestamp_file(directory, filename, file_extension, timestamp)

        with open(filepath, 'w') as file_handler:
            if filename == 'Samantha':
                raise OSError('its samm')
            file_handler.write(user_info)
    except OSError:
        print('error)')
        restore_file_from_timestamp(directory, filename, file_extension, timestamp)
        module_logger.error("Error while saving report at filepath: " + filepath)
