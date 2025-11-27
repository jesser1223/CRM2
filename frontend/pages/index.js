import Link from 'next/link'

export default function Home() {
  return (
    <div style={{ padding: 20 }}>
      <h1>CRM Dashboard</h1>
      <nav>
        <ul>
          <li><Link href="/companies">Companies</Link></li>
          <li><Link href="/contacts">Contacts</Link></li>
          <li><Link href="/deals">Deals</Link></li>
          <li><Link href="/tasks">Tasks</Link></li>
        </ul>
      </nav>
    </div>
  )
}
