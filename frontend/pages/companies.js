import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Companies() {
  const [companies, setCompanies] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/companies')
      .then(res => setCompanies(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Companies</h1>
      <ul>
        {companies.map(c => <li key={c.id}>{c.name}</li>)}
      </ul>
    </div>
  )
}
