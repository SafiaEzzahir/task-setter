import React from 'react';
import './App.css';
import TaskList from './components/Tasks';

const App = () => {
  return (
    <div className='App'>
      <header className='App-header'>
        <h1>safia's task setter</h1>
      </header>
      <main>
        <TaskList />
        <a href="mainpage.html">see all lists</a>
      </main>
    </div>
  );
};

export default App;