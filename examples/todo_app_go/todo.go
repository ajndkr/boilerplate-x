package main

import (
	"fmt"
)

type Todo struct {
	ID          int
	Title       string
	Description string
	Completed   bool
}

var todos []Todo

func addTodo(todo Todo) {
	todos = append(todos, todo)
}

func getTodos() []Todo {
	return todos
}

func getTodoByID(id int) Todo {
	for _, todo := range todos {
		if todo.ID == id {
			return todo
		}
	}
	return Todo{}
}

func updateTodoByID(id int, updatedTodo Todo) {
	for i, todo := range todos {
		if todo.ID == id {
			todos[i] = updatedTodo
			return
		}
	}
}

func deleteTodoByID(id int) {
	for i, todo := range todos {
		if todo.ID == id {
			todos = append(todos[:i], todos[i+1:]...)
			return
		}
	}
}

func main() {
	todo1 := Todo{ID: 1, Title: "Buy groceries", Description: "Milk, bread, eggs", Completed: false}
	todo2 := Todo{ID: 2, Title: "Do laundry", Description: "Wash clothes", Completed: false}

	addTodo(todo1)
	addTodo(todo2)

	fmt.Println(getTodos())

	updateTodoByID(1, Todo{ID: 1, Title: "Buy groceries", Description: "Milk, bread, eggs, cheese", Completed: false})

	fmt.Println(getTodoByID(1))

	deleteTodoByID(2)

	fmt.Println(getTodos())
}
