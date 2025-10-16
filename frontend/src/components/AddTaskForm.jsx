import React, { useState } from 'react';

const AddTaskForm = ({ addTask }) => {
    const [taskName, setTaskName] = useState('');
    const [desc, setDesc] = useState('');
    const [daysToComplete, setDaysToComplete] = useState('');
    const [author, setAuthor] = useState('')
    const [anonymous, setAnonymous] = useState(false)

    const handleSubmit = (event) => {
        event.preventDefault();
        if (taskName && desc && daysToComplete && (author || anonymous)) {
            const finalAuthor = anonymous ? "anonymous" : author;

            addTask({name: taskName, desc: desc, days_to_complete: parseInt(daysToComplete), author: finalAuthor}); // add a full Task object
            
            // reset form fields
            setTaskName('');
            setDesc('');
            setDaysToComplete('');
            setAuthor('');
            setAnonymous(false);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type='text'
                value={taskName}
                onChange={(e) => setTaskName(e.target.value)}
                placeholder='what should safia do?'
            />
            <input
                type='text'
                value={desc}
                onChange={(e) => setDesc(e.target.value)}
                placeholder='um... details pls?'
            />
            <input
                type='number'
                value={daysToComplete}
                onChange={(e) => setDaysToComplete(e.target.value)}
                placeholder='how long to i have (in days)'
                min="1"
            />
            <input 
                type="text" 
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                placeholder='who are you -_-'
            />
            <input
                type="checkbox"
                value={anonymous}
                onChange={(e) => setAnonymous(e.target.checked)}
                name='anonymous'
            />
            <label htmlFor="">stay anonymous</label>
            <button type="submit">add task</button>
        </form>
    );
};

export default AddTaskForm;