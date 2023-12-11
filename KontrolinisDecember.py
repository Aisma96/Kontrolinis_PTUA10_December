task_list = []
task_dict = {}

# def tasks():
while True:
    print('\nOptions for to-do list:')
    print('1. Add task to a list')
    print('2. Display task with due date')
    print('3. Delete task')
    print('4. Search task')
    print('5. Edit task')
    print('6. Task accomplished')
    print('7. Exiting task list!')
    option = int(input('\nChoose an option number from 1 to 7: '))
    if option == 1:
        task = input('Enter a task: ')
        due_date = input('Enter due date (YYYY-MM-DD): ')
        task_list.append(task)
    elif option == 2:
        task_number = 1
        for job in task_list:
            print(f'Task list: \n{task_number}. {job} (Due {due_date})')
            task_number += 1
    elif option == 3:
        delete = input('Exact task name: ')
        print(f'{task_list.remove(delete)} task removed from a list.')
    elif option == 4:
        x = input('task index:')
        if x in task_list:
            print(task)
        # print([task_in_list for task_in_list in task_list if input('task index:') in task_in_list])
    elif option == 5:
        task_dict[task] = due_date
        for key, value in list(task_dict.items()):
            x = input('Enter a task name: ')
            if x == task:
                new_key = input('Enter new task: ')
                new_value = input('Enter new due date (YYY-MM-DD): ')
                task_dict[new_key] = task_dict.pop(x)
                task_dict[new_value] = task_dict.pop(x)
                print(task_dict)
            else:
                print("Task does not exist.")
    elif option == 6:
        done_task = task_list[int(input('which task is done?: '))]
        task_list.remove(done_task)
        print(f'{done_task} task is accomplished and removed from list.')
    elif option == 7:
        print('You are exiting the task list.')
        break
    else:
        print('Please enter a valid option number between 1 and 7.')