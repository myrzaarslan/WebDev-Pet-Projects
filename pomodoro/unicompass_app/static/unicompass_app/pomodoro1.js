document.addEventListener("DOMContentLoaded", function () {

    let taskIdCounter = 0;

    function taskButton() {
        document.querySelector('#task-list').style.display = 'block';
    }

    function taskForm() {
        document.querySelector('#task-list').style.display = 'none';
    }

    function addTask() {
        taskButton();

        const taskInput = document.getElementById('task-input');
        const taskText = taskInput.value.trim();

        if (taskText === '') {
            alert('Please enter a task.');
            return;
        }

        taskIdCounter++;
        createTaskElement(taskIdCounter, taskText);
        saveTasksToLocalStorage();
        taskInput.value = '';
    }

    document.getElementById('add-task-button').onclick = addTask;

    function createTaskElement(id, text) {
        const decorDiv = document.createElement('div');
        decorDiv.className = 'card w-75';
        decorDiv.id = `task-id-${id}`;
        decorDiv.draggable = "true";

        const taskDiv = document.createElement('div');
        taskDiv.className = 'card-body';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';

        const taskSpan = document.createElement('span');
        taskSpan.textContent = text;

        const taskInputEdit = document.createElement('input');
        taskInputEdit.type = 'text';
        taskInputEdit.value = text;
        taskInputEdit.style.display = 'none';

        const notesDiv = document.createElement('div');
        notesDiv.role = 'alert';
        notesDiv.className = 'alert alert-warning';
        notesDiv.style.display = 'none';

        const buttonDiv = document.createElement('div');

        const notesInput = document.createElement('input');
        notesInput.type = 'text';
        notesInput.style.display = 'none';

        const editButton = document.createElement('button');
        editButton.textContent = 'Edit';
        editButton.className = "btn btn-success green-button";
        editButton.style = "marginRight: 5px;";
        editButton.onclick = function() {
            taskSpan.style.display = 'none';
            taskInputEdit.style.display = 'inline';
            saveButton.style.display = 'inline';
            editButton.style.display = 'none';
        };

        const notesButton = document.createElement('button');
        notesButton.textContent = 'Notes';
        notesButton.className = "btn btn-warning";
        notesButton.onclick = function() {
            notesDiv.style.display = 'none';
            notesInput.style.display = 'inline';
            saveNotesButton.style.display = 'inline';
            notesButton.style.display = 'none';
        };

        const saveButton = document.createElement('button');
        saveButton.textContent = 'Save';
        saveButton.className = "btn btn-success";
        saveButton.style.display = 'none';
        saveButton.onclick = function() {
            const newTaskText = taskInputEdit.value.trim();
            if (newTaskText !== '') {
                taskSpan.textContent = newTaskText;
                saveTasksToLocalStorage();
            }
            taskSpan.style.display = 'inline';
            taskInputEdit.style.display = 'none';
            saveButton.style.display = 'none';
            editButton.style.display = 'inline';
        };

        const saveNotesButton = document.createElement('button');
        saveNotesButton.textContent = 'Save';
        saveNotesButton.style.display = 'none';
        saveNotesButton.onclick = function() {
            const notes = notesInput.value.trim();
            notesDiv.textContent = notes;
            notesDiv.style.display = notes === '' ? 'none' : 'block';
            notesInput.style.display = 'none';
            saveNotesButton.style.display = 'none';
            notesButton.style.display = 'inline';
            saveTasksToLocalStorage();
        };

        buttonDiv.appendChild(editButton);
        buttonDiv.appendChild(saveButton);
        buttonDiv.appendChild(notesButton);
        
        taskDiv.appendChild(checkbox);
        taskDiv.appendChild(taskSpan);
        taskDiv.appendChild(taskInputEdit);
        taskDiv.appendChild(buttonDiv);
        taskDiv.appendChild(notesDiv);
        taskDiv.appendChild(notesInput);
        taskDiv.appendChild(saveNotesButton);

        decorDiv.appendChild(taskDiv);

        const taskList = document.getElementById('task-list');
        taskList.appendChild(decorDiv);

        checkbox.addEventListener('change', function() {
            if (this.checked) {
                taskSpan.innerHTML = `<del>${taskSpan.textContent}</del>`;
            } else {
                taskSpan.innerHTML = taskSpan.textContent;
            }
            saveTasksToLocalStorage();
        });

        decorDiv.addEventListener('dragstart', function(event) {
            event.dataTransfer.setData('text/plain', decorDiv.id);
            decorDiv.classList.add('dragging');
        });

        decorDiv.addEventListener('dragend', function() {
            decorDiv.classList.remove('dragging');
        });

        decorDiv.addEventListener('dragover', function(event) {
            event.preventDefault();
            decorDiv.classList.add('drag-over');
        });

        decorDiv.addEventListener('dragleave', function() {
            decorDiv.classList.remove('drag-over');
        });

        decorDiv.addEventListener('drop', function(event) {
            event.preventDefault();
            const droppedElementId = event.dataTransfer.getData('text/plain');
            const droppedElement = document.getElementById(droppedElementId);
            const referenceElement = decorDiv;
            if (referenceElement !== droppedElement) {
                const taskList = document.getElementById('task-list');
                const rect = referenceElement.getBoundingClientRect();
                const offset = event.clientY - rect.top;
                if (offset < rect.height / 2) {
                    taskList.insertBefore(droppedElement, referenceElement);
                } else {
                    taskList.insertBefore(droppedElement, referenceElement.nextSibling);
                }
                saveTasksToLocalStorage();
            }
            decorDiv.classList.remove('drag-over');
        });
    }

    function loadTasksFromLocalStorage() {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            const taskId = task.id.split('-')[2];
            createTaskElement(taskId, task.text);
            const taskElement = document.getElementById(task.id);
            if (task.checked) {
                taskElement.querySelector('input[type="checkbox"]').checked = true;
                taskElement.querySelector('span').innerHTML = `<del>${taskElement.querySelector('span').textContent}</del>`;
            }
            taskElement.querySelector('.alert').textContent = task.notes;
            if (task.notes) {
                taskElement.querySelector('.alert').style.display = 'block';
            }
        });
        showClearTasksButton(); // Check visibility of the clear tasks div after loading tasks
    }

    function saveTasksToLocalStorage() {
        const tasks = [];
        document.querySelectorAll('.card.w-75').forEach(task => {
            const taskId = task.id;
            const taskText = task.querySelector('span').textContent; // Use textContent here
            const notesText = task.querySelector('.alert').textContent;
            const isChecked = task.querySelector('input[type="checkbox"]').checked;
            tasks.push({ id: taskId, text: taskText, notes: notesText, checked: isChecked });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
        showClearTasksButton(); // Check if all tasks are completed and show button if necessary
    }

    function showClearTasksButton() {
        const allTasksCompleted = [...document.querySelectorAll('.card.w-75')].every(task => {
            return task.querySelector('input[type="checkbox"]').checked;
        });

        const clearTasksDiv = document.getElementById('clear-all-tasks');
        if (allTasksCompleted && document.querySelectorAll('.card.w-75').length > 0) {
            clearTasksDiv.style.display = 'block';
        } else {
            clearTasksDiv.style.display = 'none';
        }
    }

    function clearAllTasks() {
        document.querySelectorAll('.card.w-75').forEach(task => task.remove());
        localStorage.removeItem('tasks'); // Clear tasks from localStorage
        showClearTasksButton();
        triggerConfettiAnimation(); // Trigger the confetti animation when all tasks are cleared
    }

    function triggerConfettiAnimation() {
        const duration = 15 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {
            return Math.random() * (max - min) + min;
        }

        const interval = setInterval(function() {
            const timeLeft = animationEnd - Date.now();

            if (timeLeft <= 0) {
                return clearInterval(interval);
            }

            const particleCount = 50 * (timeLeft / duration);

            confetti(
                Object.assign({}, defaults, {
                    particleCount,
                    origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
                })
            );
            confetti(
                Object.assign({}, defaults, {
                    particleCount,
                    origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
                })
            );
        }, 250);
    }

    let currentTimer = "pomodoro";  // Default timer is pomodoro
    let isRunning = false;
    let interval;  // To store the interval reference

    const timers = {
        pomodoro: { time: 25 * 60, defaultTime: 25 * 60, element: document.getElementById("pomodoroTime") },
        shortBreak: { time: 5 * 60, defaultTime: 5 * 60, element: document.getElementById("shortBreak") },
        longBreak: { time: 15 * 60, defaultTime: 15 * 60, element: document.getElementById("longBreak") }
    };

    const displayTimer = document.getElementById("display-timer");
    const startButton = document.getElementById("button-timer");

    function updateDisplay(time) {
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;
        displayTimer.innerHTML = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    }

    function resetTimer(timerType) {
        if (timers[timerType]) {
            timers[timerType].time = timers[timerType].defaultTime;
            updateDisplay(timers[timerType].time);
        } else {
            console.error(`Timer type ${timerType} not found`);
        }
    }
    
    document.querySelectorAll('.nav-link').forEach(button => {
        button.addEventListener('click', () => {
            stopTimer();  // Stop the timer when changing modes
    
            currentTimer = button.id;  // Set the current timer to the selected mode
            resetTimer(currentTimer);  // Reset the current timer to its default time
    
            // Update button styles to show active mode
            document.querySelectorAll('.nav-link').forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
    

    function startTimer() {
        if (isRunning) return;

        isRunning = true;
        startButton.innerHTML = "STOP";
        startButton.classList.remove("btn-primary");
        startButton.classList.add("btn-danger");

        interval = setInterval(() => {
            if (timers[currentTimer].time > 0) {
                timers[currentTimer].time--;
                updateDisplay(timers[currentTimer].time);
            } else {
                clearInterval(interval);
                resetTimer(currentTimer);
                isRunning = false;
                startButton.innerHTML = "START";
                startButton.classList.remove("btn-danger");
                startButton.classList.add("btn-primary");
                alert("Time's up!");
            }
        }, 1000);
    }

    function stopTimer() {
        if (!isRunning) return;

        clearInterval(interval);  // Stop the current interval
        isRunning = false;
        startButton.innerHTML = "START";
        startButton.classList.remove("btn-danger");
        startButton.classList.add("btn-primary");
    }

    // Handle clicking the start/stop button
    startButton.addEventListener("click", () => {
        if (isRunning) {
            stopTimer();  // Stop the timer if running
        } else {
            startTimer();  // Start the timer if not running
        }
    });

    // Initially set the display for the default Pomodoro timer
    updateDisplay(timers[currentTimer].time);
    loadTasksFromLocalStorage();
    document.getElementById('clear-tasks-button').onclick = clearAllTasks;
});


