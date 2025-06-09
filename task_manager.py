from datetime import datetime
import json


task_list = []

TASK_FIELDS = ['id', 'title', 'tag', 'priority', 'done', 'created']
EDITABLE_FIELDS = ['title', 'tag', 'priority', 'done']


def add_task(task=None):
    """добавляем задачу в список"""
    task = {}
    task['id'] = get_next_id()
    task['title'] = input("Введите заголовок задачи: ")
    task['tag'] = input("Введите тег задачи: ")
    task['done'] = False
    task['priority'] = valid_priority()
    task['created'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    task_list.append(task)

    
def list_tasks():
    """вывод всех задач с нумерацией"""
    for i, task in enumerate(task_list, start=1):
        print(f'{i} {task}')

def delete_task(delete_ind):
    """удаление задачи по номеру"""
    try:
        if 1 <= delete_ind <= len(task_list):
            task_list.pop(delete_ind - 1)
    except IndexError:
        print("Введено неверное число.")
    except ValueError:
        print("Неверный формат данных. Введите число: ")

def edit_task(task_id):
    """редактирование задачи"""
    task = find_task_by_id(task_id)
    if task is None:
        print('Задача не найдена')
        return

    for key in TASK_FIELDS:
        print(f'{key}: {task.get(key)}')

    for key in EDITABLE_FIELDS:
        print(f'Изменить ключ: {key} y/n')
        answer = input().strip().lower()
        if answer == 'y':
            if key == 'priority':
                task[key] = valid_priority()
            elif key == 'done':
                done_input = input('Задача выполнена? (y/n): ').lower()
                task[key] = True if done_input == 'y' else False
            else:
                task[key] = input(f'Введите новое значение для {key}: ')

    print("Обновлённая задача:")
    for key in TASK_FIELDS:
        print(f'{key}: {task.get(key)}')

    save_tasks_to_file("tasks.json")
    print("Задача успешно обновлена и сохранена в файл.")

    
def save_tasks_to_file(filename): 
    """сохранение задачи в файл"""
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(task_list, file, ensure_ascii=False, indent=2)
            print(f"{filename} успешно записан")
    except OSError:
        print('Ошибка при работе с файлом')

def load_tasks_from_file(filename):
    """загрузка задач из файла"""
    task_list.clear()
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            task_list.extend(data)
        print('Задачи успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    except OSError:
        print('Ошибка при работе с файлом')
        
def get_next_id():
    """создаём корректный ID для задачи"""
    if not task_list:
        return 1
    return max(task["id"] for task in task_list) + 1

def valid_priority():
    """проверка правильного приоритета"""
    allowed_priorities = ["low", "medium", "high"]
    while True:        
        priority = input("Введите приоритет задачи (low/medium/high): ").lower()
        if priority in allowed_priorities:
            return priority
        print('Ошибка: приоритет должен быть low, medium или high.')

def find_task_by_id(task_id):
    """поиск задачи по id"""
    for task in task_list:
        if task["id"] == task_id:
            return task
    return None

    