package main

import (
	"fmt"
)

type Todo struct {
	ID          int
	Description string
	Completed   bool
}

func main() {
	fmt.Println("Welcome to the Todo App!")
}
