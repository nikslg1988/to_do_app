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

def edit_task(task_number, new_text): 
    """редактирование задачи"""  
    if 1 <= task_number <= len(task_list):
        task_list[task_number - 1] = new_text
        print(f"Задача №{task_number} обновлена")
    else:
        print("Задачи с таким номером не существует")
   
def save_tasks_to_file(filename): 
    """сохранение задачи в файл"""
    try:
        with open(filename, 'w') as file:
            for item in task_list:
                file.write(item + '\n')
            print(f"{filename} успешно записан")
    except OSError:
        print('Ошибка при работе с файлом')

def load_tasks_from_file(filename): #TODO 
    """Загрузка задач из файла"""
    task_list.clear()
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_list.append(line.strip('\n'))
        print('Задачи успешно загружены')
    except FileNotFoundError:
        print('Файл не найден')
    except OSError:
        print('Ошибка при работе с файлом')
           
    
    
task = str(input())

