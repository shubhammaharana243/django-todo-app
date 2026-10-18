
document.addEventListener("DOMContentLoaded", function () {

    const addTaskBtn = document.querySelector(".add-task-btn");
    const taskForm = document.querySelector("#add-task-form");
    const updateTaskForm = document.querySelector("#update-task-form");
    const taskInput = document.querySelector("#task-title");
    const updateTaskInput = document.querySelector("#update-task-title");
    const taskList = document.querySelector("#task-list");
    const cancelTaskBtn = document.querySelector(".cancel-task-btn");
    const editButtons = document.querySelectorAll(".edit-task-btn");
    const completeTaskForm = document.querySelector("#complete_task-form")   
    const search = document.querySelector(".nav-serch .nav-search");
    const toggle = document.querySelector(".mobile-search-toggle");
    const input = document.querySelector(
        ".nav-serch .search-form input[name='search']"
    );


    if (search && toggle && input) {
        toggle.addEventListener("click", function () {
            const isOpen = search.classList.toggle("search-open");

            toggle.setAttribute("aria-expanded", String(isOpen));
            toggle.setAttribute(
                "aria-label",
                isOpen ? "Close search" : "Open search"
            );

            if (isOpen) {
                input.focus();
            }
        });
    } else {
        console.error("Mobile search elements not found");
    }


    // OPEN ADD TASK FORM

    addTaskBtn.addEventListener("click", function () {
        taskForm.hidden = false;
        taskInput.focus();
    });

    // CANCEL TASK FORM

    cancelTaskBtn.addEventListener("click", function () {
        taskForm.reset();
        taskForm.hidden = true;

    });

    // CREATE TASK

    taskForm.addEventListener("submit", function () {

        const taskName = taskInput.value.trim();

        if (taskName === "") {
            alert("Please enter a task!");
            taskInput.focus();
            return;
        }
        taskForm.hidden = true;

    });
    
editButtons.forEach(function (button) {
    button.addEventListener("click", function () {

        const taskId = button.dataset.taskId;
        const taskTitle = button.dataset.taskTitle;

        updateTaskForm.action = `/todo/update/${taskId}/`;

        updateTaskInput.value = taskTitle;

        updateTaskForm.hidden = false;

    });
});

// updateTaskForm.addEventListener("submit", function (event) {
//     const taskTitle = updateTaskInput.value.trim();

//     if (taskTitle === "") {
//         event.preventDefault();
//         alert("Please enter an updated task!");
//         updateTaskInput.focus();
//     }
// });

completeTaskBtn.forEach(function(button){
    button.addEventListener("click", function(){
        const taskId = button.dataset.taskId

        completeTaskForm.action = `/todo/iscompleted/${taskId}`

    })
})

    // EDIT TASK

    taskList.addEventListener("click", function (event) {
        const button = event.target.closest("button");

        if (!button) return;

        const row = button.closest("tr");

        if (!row) return;

        if (button.classList.contains("edit-task-btn")) {
            editingRow = row;

            taskInput.value =
                row.querySelector(".task-name").textContent.trim();

            updateTaskForm.hidden = false;
            taskForm.hidden = true;

            taskInput.focus();
        }

    });

    

    
        
});

