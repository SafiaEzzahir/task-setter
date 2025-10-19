import React, { useEffect, useState } from 'react';
import api from "../api.js";
import AddTaskForm from './AddTaskForm';

const TaskList = () => {
    const [tasks, setTasks] = useState([]);

    const fetchTasks = async () => {
        try {
            console.log('fetching tasks');
            const response = await api.get('/tasks');
            setTasks(response.data);
        } catch (error) {
            console.error("error fetching tasks", error);
        }
    };

    const addTask = async (task) => {
        try {
            console.log(task);
            await api.post('/tasks', task);
            fetchTasks(); // refresh list display after 
        } catch (error) {
            console.error("error adding task", error);
        }
    };

    const deleteTask = async (task_id) => {
        try {
            console.log("deleting task:", task_id)
            await api.delete(`/tasks/${task_id}`);
            fetchTasks(); // refresh list display after
        } catch (error) {
            console.error("error deleting task", error);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div>
            <h2>safia's tasks</h2>
            <ul>
                {tasks?.map((task, index) => (
                    <li key={index}>
                        <div>
                            <p className="name">{task.name}</p>
                            <p className="desc">{task.desc}</p>
                            <p className="days">{task.days_to_complete} day(s) left</p>
                            <p className="author">set by {task.author}</p>
                            <button
                                onClick={() => deleteTask(task.id)}
                                title='delete task'
                            >delete task</button>
                        </div>
                    </li>
                ))}
            </ul>
            <AddTaskForm addTask={addTask} />
        </div>
    );
};

export default TaskList;