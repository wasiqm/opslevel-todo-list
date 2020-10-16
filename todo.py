# create new items, delete existing items, and list all of my current items to do
class Todo:
    def __init__(self):
        self.todo_list = {}

    def get_todo_list(self):
        return self.todo_list

    def add_item(self, item_to_add, priority):
        if item_to_add not in self.todo_list:
            self.todo_list[item_to_add] = priority
            return 'Item successfully added.'
        else:
            return 'Item already exists.'

    def delete_item(self, item_to_delete):
        if item_to_delete in self.todo_list:
            del self.todo_list[item_to_delete]
            return 'Item successfully deleted.'
        else:
            return 'Item does not exist.'

    def get_repeat_priorities(self):
        flipped = {}
        for task, priority in self.todo_list.items():
            if priority not in flipped: 
                flipped[priority] = [task] 
            else: 
                flipped[priority].append(task)

        repeated = {}
        for priority, tasks in flipped.items():
             if len(tasks) > 1:
                repeated[priority] = tasks
        return repeated