import React, { useState } from 'react';
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:8001';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [sessions, setSessions] = useState([]);

  const register = async () => {
    const res = await axios.post('/register', { username, password });
    console.log(res.data);
  };

  const login = async () => {
    const res = await axios.post('/login', { username, password });
    console.log(res.data);
  };

  const createSession = async () => {
    const res = await axios.post('/session', { date: '2022-01-01', time: '10:00', place: 'Yoga Studio', max_participants: 10 });
    console.log(res.data);
  };

  const listSessions = async () => {
    const res = await axios.get('/sessions');
    setSessions(res.data);
  };

  const bookSession = async (session_id) => {
    const res = await axios.post(`/book/${session_id}`);
    console.log(res.data);
  };

  return (
    <div className='App'>
      <input type='text' value={username} onChange={(e) => setUsername(e.target.value)} placeholder='Username' />
      <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Password' />
      <button onClick={register}>Register</button>
      <button onClick={login}>Login</button>
      <button onClick={createSession}>Create Session</button>
      <button onClick={listSessions}>List Sessions</button>
      {sessions.map((session, index) => (
        <div key={index}>
          <p>{session.date} {session.time} {session.place} {session.max_participants} {session.booked_participants}</p>
          <button onClick={() => bookSession(index)}>Book</button>
        </div>
      ))}
    </div>
  );
}

export default App;
