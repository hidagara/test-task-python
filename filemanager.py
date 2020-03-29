import os
import time
import logging

module_logger = logging.getLogger("reports_application")


def init_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def create_timestamp_file(directory, filename, file_extension, timestamp):
    filepath = directory + '/' + filename
    module_logger.info("Trying to create timestamp file at: " + filepath)
    if os.path.isfile(filepath + file_extension):
        module_logger.info("Create timestamp file at: " + filepath + '_' + timestamp + file_extension)
        os.replace(filepath + file_extension, filepath + '_' + timestamp + file_extension)


def restore_file_from_timestamp(directory, filename, file_extension, timestamp):
    filepath = directory + '/' + filename
    timestamp_filepath = filepath + '_' + timestamp + file_extension
    module_logger.info("Trying to restore file from timestamp: " + timestamp_filepath)
    if os.path.isfile(timestamp_filepath):
        module_logger.info("Restore file: " + timestamp_filepath + " in " + filepath + file_extension)
        os.replace(timestamp_filepath, filepath + file_extension)


def write_userinfo(user_info, directory, filename):
    module_logger.info("Start writing info for: " + filename)
    file_extension = '.txt'

    filepath = directory + '/' + filename + file_extension
    timestamp = ''

    if os.path.isfile(filepath):
        file_mod_time = time.localtime(os.path.getmtime(filepath))
        timestamp = time.strftime("%Y-%m-%dT%H:%M", file_mod_time)
        create_timestamp_file(directory, filename, file_extension, timestamp)
    try:
        with open(filepath, 'w') as file_handler:
            file_handler.write(user_info)
            module_logger.info("Info has been written into: " + filepath)
    except OSError as e:
        restore_file_from_timestamp(directory, filename, file_extension, timestamp)
        module_logger.error("Error while saving report at filepath: " + filepath)
        module_logger.error(e)
