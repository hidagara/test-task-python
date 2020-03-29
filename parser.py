import requests
import json
import sys
from user import User
import filemanager
import logging


def main():
    logger = logging.getLogger("reports_application")
    logger.setLevel(logging.ERROR)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("reports_log.txt")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s: %(message)s',
                                  datefmt="%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        logger.info("Start parsing users")
        user_response = requests.get('https://json.medrating.org/users')
        user_response.raise_for_status()
        logger.info("Users has been parsed successfully")
    except requests.exceptions.RequestException as e:
        logger.error(e)
        raise sys.exit(e)

    try:
        logger.info("Start parsing tasks")
        task_response = requests.get('https://json.medrating.org/todos')
        task_response.raise_for_status()
        logger.info("Tasks has been parsed successfully")
    except requests.exceptions.RequestException as e:
        logger.error(e)
        raise sys.exit(e)

    user_list = json.loads(user_response.text)
    task_list = json.loads(task_response.text)

    if len(user_list) == 0:
        logger.error("No users for report")
        sys.exit()
    if len(task_list) == 0:
        logger.error("No tasks for report")
        sys.exit()

    directory_name = 'tasks'
    filemanager.init_directory(directory_name)

    for user in user_list:
        current_user = User(user['id'],
                            user['name'],
                            user['username'],
                            user['email'],
                            user['company']['name'])
        current_user.fill_user_with_tasks(task_list)
        user_info = current_user.get_user_info()
        filename = current_user.username
        filemanager.write_userinfo(user_info, directory_name, filename)


if __name__ == '__main__':
    main()
