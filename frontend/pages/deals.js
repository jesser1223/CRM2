import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Deals() {
  const [deals, setDeals] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/deals')
      .then(res => setDeals(res.data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Deals</h1>
      <ul>
        {deals.map(d => <li key={d.id}>{d.name} - {d.stage}</li>)}
      </ul>
    </div>
  )
}
