document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("taskInput").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            addTask();
        }
    });
});

function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    
    if (taskText === "") return;

    let taskList = document.getElementById("taskList");
    
    let li = document.createElement("li");
    li.innerHTML = `
        <span onclick="toggleTask(this)">${taskText}</span>
        <button class="delete-btn" onclick="removeTask(this)">X</button>
    `;
    
    taskList.appendChild(li);
    taskInput.value = "";
}

function toggleTask(element) {
    element.classList.toggle("completed");
}

function removeTask(button) {
    button.parentElement.remove();
}