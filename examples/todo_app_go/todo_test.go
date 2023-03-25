package main

import (
	"testing"
)

func TestAddTodoItem(t *testing.T) {
	todo := NewTodo()
	todo.AddTodoItem("Buy groceries")
	if len(todo.items) != 1 {
		t.Errorf("Expected 1 item, but got %d", len(todo.items))
	}
}

func TestRemoveTodoItem(t *testing.T) {
	todo := NewTodo()
	todo.AddTodoItem("Buy groceries")
	todo.RemoveTodoItem(0)
	if len(todo.items) != 0 {
		t.Errorf("Expected 0 items, but got %d", len(todo.items))
	}
}

func TestGetTodoItems(t *testing.T) {
	todo := NewTodo()
	todo.AddTodoItem("Buy groceries")
	todo.AddTodoItem("Do laundry")
	items := todo.GetTodoItems()
	if len(items) != 2 {
		t.Errorf("Expected 2 items, but got %d", len(items))
	}
	if items[0] != "Buy groceries" {
		t.Errorf("Expected 'Buy groceries', but got '%s'", items[0])
	}
	if items[1] != "Do laundry" {
		t.Errorf("Expected 'Do laundry', but got '%s'", items[1])
	}
}
