// Define the tasks array
let tasks = [];

// Define the addTask function
function addTask(task) {
  tasks.push(task);
}

// Define the removeTask function
function removeTask(task) {
  const index = tasks.indexOf(task);
  if (index > -1) {
    tasks.splice(index, 1);
  }
}

// Define the displayTasks function
function displayTasks() {
  const taskList = document.getElementById("task-list");
  taskList.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.innerText = task;
    taskList.appendChild(li);
  });
}

// Define the clearInput function
function clearInput() {
  document.getElementById("task-input").value = "";
}

// Define the addTaskButton event listener
document.getElementById("add-task-button").addEventListener("click", () => {
  const taskInput = document.getElementById("task-input");
  const task = taskInput.value.trim();
  if (task !== "") {
    addTask(task);
    displayTasks();
    clearInput();
  }
});

// Define the removeTaskButton event listener
document.getElementById("remove-task-button").addEventListener("click", () => {
  const taskInput = document.getElementById("task-input");
  const task = taskInput.value.trim();
  if (task !== "") {
    removeTask(task);
    displayTasks();
    clearInput();
  }
});
