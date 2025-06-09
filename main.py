
import sys
from task_manager import add_task, list_tasks, delete_task, edit_task, save_tasks_to_file, load_tasks_from_file
while True:
    # Меню
    print("Меню:")
    print("1. Добавить Задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу")
    print("4. Редактировать задачу")
    print("5. Сохранить задачи в файл")
    print("6. Загрузить задачи из файла")
    print("0. Выход")
    
    sys.stdout.flush()

    # Ввод пользователя
    try:
        choice_func = int(input("Выберите функцию: "))
    except ValueError:
        print("Введите корректное число!")
        continue  # Если пользователь ввел не число, пропустим текущую итерацию и повторим запрос
    # Обработка выбора
    if choice_func == 1:
        add_task(input("Введите текст задачи: "))
    elif choice_func == 2:
        list_tasks()
    elif choice_func == 3:
        try:
            task_number = int(input("Удалить задачу (укажите номер): "))
            delete_task(task_number)
        except ValueError:
            print("Номер задачи должен быть числом!")
    elif choice_func == 4:
        try:
            task_number = int(input("Укажите номер задачи для редактирования: "))
            new_text = input("Введите новый текст задачи: ")
            edit_task(task_number, new_text)
        except ValueError:
            print("Номер задачи должен быть числом!")
    elif choice_func == 5:
        save_tasks_to_file(input("Укажите имя файла для сохранения *.json: "))
    elif choice_func == 6:
        load_tasks_from_file(input("Укажите имя файла для загрузки *.json: "))
    elif choice_func == 0:
        break  # Выход из программы
