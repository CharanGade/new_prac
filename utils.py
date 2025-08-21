def print_task(index, task):
    status = "✓" if task['done'] else "✗"
    print(f"{index}. [{status}] {task['task']}")
