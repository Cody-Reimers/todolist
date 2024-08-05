
import data_validation as dv
from todo import Todo

###############################################################################



###############################################################################

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def __str__(self):
        lines = [f"----- {self.title} -----"]
        lines += [ str(item) for item in self._todos ]

        return "\n".join(lines)

    def __len__(self):
        return len(self._todos)

    def to_list(self):
        return self._todos[:]

    @property
    def title(self):
        return self._title

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def todo_at(self, index):
        return self._todos[index]

    def add(self, other):
        ref = "Todo List Element Object"

        if not isinstance(other, Todo):
            raise TypeError(f"{repr(ref)} must be of type 'Todo'!")

        self._todos.append(other)

    def remove_at(self, index):
        del self._todos[index]

    def mark_done_at(self, index):
        self._todos[index].is_done = True

    def mark_all_done(self):
        def mark_done(todo):
            todo.is_done = True

        self.each(mark_done)

    def mark_undone_at(self, index):
        self._todos[index].is_done = False

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.is_done = False

        self.each(mark_undone)

    def all_done(self):
        return all([ item.is_done for item in self._todos ])

    def each(self, callback):
        for item in self._todos:
            callback(item)

    def select(self, callback):
        new_list = TodoList(self.title)

        [ new_list.add(item) for item in self._todos if callback(item) ]

        return new_list

    def find_by_title(self, name):
        for item in self._todos:
            if item.name == name:
                return item

        raise IndexError("No such item in Todo List!")

    def done_todos(self):
        return self.select(lambda todo: todo.is_done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.is_done)

    def mark_done(self, name):
        found = self.find_by_title(name)
        found.is_done = True

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#//////////////////////////////////////////////////////////////////////////////

###############################################################################


