
import unittest
from todo import Todo
from todolist import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                         self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add(self):
        bad_data = [1, "hi", TodoList("Test"), {1: Todo("Test")}]

        for item in bad_data:
            self.assertRaises(TypeError, self.todos.add, item)

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(self.todo2, self.todos.todo_at(1))
        self.assertEqual(self.todo3, self.todos.todo_at(2))
        self.assertRaises(IndexError, self.todos.todo_at, 4)

    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(4)

        self.todos.mark_done_at(1)
        self.assertFalse(self.todo1.is_done)
        self.assertTrue(self.todo2.is_done)
        self.assertFalse(self.todo3.is_done)

    def test_mark_undane_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(4)

        self.todo1.is_done = True
        self.todo2.is_done = True
        self.todo3.is_done = True

        self.todos.mark_undone_at(2)
        self.assertTrue(self.todo1.is_done)
        self.assertTrue(self.todo2.is_done)
        self.assertFalse(self.todo3.is_done)

    def test_mark_all_done(self):
        self.todos.mark_all_done()

        self.assertTrue(self.todo1.is_done)
        self.assertTrue(self.todo2.is_done)
        self.assertTrue(self.todo3.is_done)
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(10)

        self.todos.remove_at(0)
        self.assertEqual([self.todo2, self.todo3], self.todos.to_list())

    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )

        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )

        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )

        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        def set_and_confirm_true(todo):
            todo.is_done = True
            self.assertTrue(todo.is_done)

        self.todos.each(set_and_confirm_true)

    def test_select(self):
        self.todos.mark_done_at(1)

        new_list = self.todos.select(lambda todo: todo.is_done)

        self.assertTrue(new_list.todo_at(0).is_done)

    # your tests go here

if __name__ == "__main__":
    unittest.main()
