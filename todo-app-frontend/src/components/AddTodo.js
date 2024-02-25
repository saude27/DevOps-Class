import React, { useState } from 'react';

function AddTodo({ onAdd }) {
  const [text, setText] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (text.trim()) {
      fetch('http://localhost:5000/api/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          setText('');
          onAdd(data); // Pass the full todo object
        })
        .catch(error => {
          console.error('Error adding todo:', error);
        });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="add-todo-form">
      <input type="text" placeholder="Add a new todo..." value={text} onChange={handleChange} />
      <button type="submit">Add</button>
    </form>
  );
}

export default AddTodo;
