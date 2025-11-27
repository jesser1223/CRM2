import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Tasks() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/tasks')
      .then(res => setTasks(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Tasks</h1>
      <ul>
        {tasks.map(t => <li key={t.id}>{t.description} - {t.status}</li>)}
      </ul>
    </div>
  )
}
