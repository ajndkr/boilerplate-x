import unittest

from todo import TodoList


class TestTodoList(unittest.TestCase):
    def test_add_item(self):
        todo_list = TodoList()
        todo_list.add_item("Buy groceries")
        self.assertEqual(todo_list.get_items(), ["Buy groceries"])

    def test_remove_item(self):
        todo_list = TodoList()
        todo_list.add_item("Buy groceries")
        todo_list.remove_item("Buy groceries")
        self.assertEqual(todo_list.get_items(), [])

    def test_get_items(self):
        todo_list = TodoList()
        todo_list.add_item("Buy groceries")
        todo_list.add_item("Do laundry")
        self.assertEqual(todo_list.get_items(), ["Buy groceries", "Do laundry"])


if __name__ == "__main__":
    unittest.main()
