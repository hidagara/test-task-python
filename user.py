import datetime


class User:
    def __init__(self, id, name, username, email, company_name, completed_tasks=None, uncompleted_tasks=None):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.company_name = company_name
        self.completed_tasks = completed_tasks
        self.uncompleted_tasks = uncompleted_tasks

    def set_completed_tasks(self, completed_tasks):
        self.completed_tasks = completed_tasks

    def set_uncompleted_tasks(self, uncompleted_tasks):
        self.uncompleted_tasks = uncompleted_tasks

    def get_completed_tasks(self):
        result = ''
        for task in self.completed_tasks:
            result += task['title'] + '\n'
        if not result:
            'Не имеется выполненных задач'
        return result

    def get_uncompleted_tasks(self):
        result = ''
        for task in self.uncompleted_tasks:
            result += task['title'] + '\n'
        if not result:
            'Не имеется невыполненных задач'
        return result

    def fill_user_with_tasks(self, tasks):
        uncompleted_tasks = []
        completed_tasks = []
        for task in tasks:
            if len(task['title']) > 50:
                task['title'] = task['title'][:50] + '...'
            if task['userId'] == self.id:
                if task['completed']:
                    completed_tasks.append(task)
                else:
                    uncompleted_tasks.append(task)
        self.set_uncompleted_tasks(uncompleted_tasks)
        self.set_completed_tasks(completed_tasks)

    def get_user_info(self):
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        info_to_write = self.username + f'<{self.email}> {now}'
        info_to_write += '\n'
        info_to_write += self.company_name
        info_to_write += '\n\n'
        info_to_write += 'Завершенные задачи:\n'
        info_to_write += self.get_completed_tasks()
        info_to_write += '\n'
        info_to_write += 'Оставшиеся задачи:\n'
        info_to_write += self.get_uncompleted_tasks()
        info_to_write += '\n'
        return info_to_write
