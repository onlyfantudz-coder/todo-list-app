#Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """thêm một công việc mới vào danh sách"""
    tasks.append(task_name)
    print(f"Đã thêm công việc:'{task_name}""")
#---Điểm bắt đầu của chương trình---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    
    tasks = []

def add_task(task_name):
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f" Đã thêm công việc: {task_name}")

def list_tasks():
    print("\n Danh sách công việc:")
    if not tasks:
        print(" (Chưa có công việc nào!)")
        return

    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f" Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print(" Chỉ số công việc không hợp lệ!")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập Python")

    list_tasks()

    print("\n--- Đánh dấu công việc 1 là hoàn thành ---")
    complete_task(0)

    list_tasks()
tasks = []

def add_task(task_name):
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f" Đã thêm công việc: {task_name}")

    print("\n Danh sách công việc:")
    if not tasks:
        print(" (Chưa có công việc nào!)")
        return

    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f" Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print(" Chỉ số công việc không hợp lệ!")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f" Đã xóa công việc: {deleted_task['name']}")
    else:
        print(" Chỉ số công việc không hợp lệ!")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập Python")
    add_task("Đọc tài liệu")

    list_tasks()

    print("\n--- Đánh dấu công việc 1 là hoàn thành ---")
    complete_task(0)
    list_tasks()

    print("\n--- Xóa công việc 2 ---")
    delete_task(1)

    list_tasks()