from task import Task
from datetime import datetime
import json

task_list = []

TASK_FIELDS = ['id', 'title', 'tag', 'priority', 'done', 'created']
EDITABLE_FIELDS = ['title', 'tag', 'priority', 'done']

def add_task(task=None): #TODO
    """добавляем задачу в список"""
    task_id = get_next_id()
    title = input("Введите заголовок задачи: ")
    tag = input("Введите тег задачи: ")
    priority = valid_priority()
    done = False
    created = datetime.now().strftime("%Y-%m-%d %H:%M")
    task = Task(task_id, title, tag, priority, done, created)  # создаем объект класса с переданными параметрами
    task_list.append(task)
    
def list_tasks():
    """вывод всех задач с нумерацией"""
    for i, task in enumerate(task_list, start=1):
        print(f'{i}. {task}')

def delete_task_by_id(task_id):
    task = find_task_by_id(task_id)
    if task:
        task_list.remove(task)
        save_tasks_to_file("tasks.json")
        print(f"Задача с id {task_id} успешно удалена")
    else:
        print("Задача не найдена")
    
def edit_task(task_id):
    """редактирование задачи"""
    print('DEBUGGER')
    task = find_task_by_id(task_id)
    if not task:
        print('Задача не найдена')
        return
    
    print('Текущая задача:')
    print(task)

    for key in EDITABLE_FIELDS:
        current_value = getattr(task, key)
        answer = input(f"Изменить {key} (текущее значение: {current_value})? (y/n): ").strip().lower()
        if answer == 'y':
            if key == 'priority':
                setattr(task, key, valid_priority())
            elif key == 'done':
                done_input = input('Задача выполнена? (y/n): ').lower()
                setattr(task, key, done_input == 'y')
            else:
                new_value = input(f'Введите новое значение для {key}: ')
                setattr(task, key, new_value)

    print("Обновлённая задача:")
    print(task)

    save_tasks_to_file("tasks.json")
    print("Задача успешно обновлена и сохранена в файл.")
  
def save_tasks_to_file(filename): 
    """сохранение задачи в файл"""
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump([task.to_dict() for task in task_list], file, ensure_ascii=False, indent=2)
            print(f"{filename} успешно записан")
    except OSError:
        print('Ошибка при работе с файлом')

def load_tasks_from_file(filename):
    """загрузка задач из файла"""
    task_list.clear()
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            task_list.extend([Task.from_dict(data) for data in data])
        print('Задачи успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    except OSError:
        print('Ошибка при работе с файлом')
        
def get_next_id():
    """создаём корректный ID для задачи"""
    if not task_list:
        return 1
    return max(task.id for task in task_list) + 1

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
        if task.id == task_id:
            return task
    return None



        
