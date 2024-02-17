import React from 'react';

function TodoItem({ todo, onUpdate, onDelete }) {
  const handleToggle = () => {
    fetch(`http://localhost:31382/api/todos/${todo.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: !todo.completed })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(updatedTodo => {
        onUpdate(updatedTodo);
      })
      .catch(error => {
        console.error('Error updating todo:', error);
      });
  };

  return (
    <li key={todo.id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
      <input type="checkbox" checked={todo.completed} onChange={handleToggle} />
      <span>{todo.text}</span>
      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </li>
  );
}

export default TodoItem;
