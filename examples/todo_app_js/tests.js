// Tests for the todo app

// Test adding a new task
function testAddTask() {
  const todoList = new TodoList();
  todoList.addTask("Buy groceries");
  assert(todoList.tasks.length === 1, "Task was not added correctly");
}

// Test completing a task
function testCompleteTask() {
  const todoList = new TodoList();
  todoList.addTask("Buy groceries");
  todoList.completeTask(0);
  assert(
    todoList.tasks[0].completed === true,
    "Task was not completed correctly"
  );
}

// Test deleting a task
function testDeleteTask() {
  const todoList = new TodoList();
  todoList.addTask("Buy groceries");
  todoList.deleteTask(0);
  assert(todoList.tasks.length === 0, "Task was not deleted correctly");
}

// Run all tests
function runTests() {
  testAddTask();
  testCompleteTask();
  testDeleteTask();
  console.log("All tests passed!");
}

runTests();
