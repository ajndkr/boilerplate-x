#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_todo() {
        let mut todo_list = TodoList::new();
        todo_list.add_todo("Buy groceries".to_string());
        assert_eq!(todo_list.todos.len(), 1);
    }

    #[test]
    fn test_remove_todo() {
        let mut todo_list = TodoList::new();
        todo_list.add_todo("Buy groceries".to_string());
        todo_list.remove_todo(0);
        assert_eq!(todo_list.todos.len(), 0);
    }

    #[test]
    fn test_mark_todo_as_done() {
        let mut todo_list = TodoList::new();
        todo_list.add_todo("Buy groceries".to_string());
        todo_list.mark_todo_as_done(0);
        assert_eq!(todo_list.todos[0].done, true);
    }
}
