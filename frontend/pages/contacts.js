import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Contacts() {
  const [contacts, setContacts] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/contacts')
      .then(res => setContacts(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Contacts</h1>
      <ul>
        {contacts.map(c => <li key={c.id}>{c.first_name} {c.last_name}</li>)}
      </ul>
    </div>
  )
}
