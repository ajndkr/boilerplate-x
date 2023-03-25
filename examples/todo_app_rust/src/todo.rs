// This file contains the implementation of the Todo struct and its methods

pub struct Todo {
    pub title: String,
    pub description: String,
    pub completed: bool,
}

impl Todo {
    pub fn new(title: String, description: String) -> Todo {
        Todo {
            title,
            description,
            completed: false,
        }
    }

    pub fn complete(&mut self) {
        self.completed = true;
    }

    pub fn uncomplete(&mut self) {
        self.completed = false;
    }
}

// This is the end of the Todo struct implementation. You can add more methods or fields as needed.
