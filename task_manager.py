task_list = []

def add_task(task):
    """добавляем задачу в список"""
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

def edit_task(): #TODO
    """редактирование задачи""" 
    pass    
    
    
task = str(input())

