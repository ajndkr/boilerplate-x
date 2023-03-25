# Simple Todo App in Golang

This is a simple todo app written in Golang. It allows you to add, view, and delete tasks from a list.

## Installation

To install this app, you need to have Golang installed on your system. You can download it from the official website [here](https://golang.org/dl/).

Once you have Golang installed, you can clone this repository and run the following command to install the dependencies:

```
go get github.com/gorilla/mux
```

## Usage

To run the app, navigate to the project directory and run the following command:

```
go run main.go
```

This will start the server on port 8080. You can access the app by navigating to `http://localhost:8080` in your web browser.

## API Endpoints

The following API endpoints are available:

- `GET /tasks` - Get all tasks
- `GET /tasks/{id}` - Get a specific task by ID
- `POST /tasks` - Add a new task
- `PUT /tasks/{id}` - Update an existing task
- `DELETE /tasks/{id}` - Delete a task

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
