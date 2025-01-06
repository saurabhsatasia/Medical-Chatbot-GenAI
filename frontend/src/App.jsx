import { useState } from 'react';
import { Layout } from './components/Layout';


function App() {
  const [count, setCount] = useState(0)

  return (
    <Layout>
      <h1 className="text-2xl font-semibold">Medical Chatbot</h1>
      <p className="text-muted-foreground">Ask me anything about medical topics</p>
      <div className="flex items-center justify-center mt-8">
        <button
          className="px-4 py-2 bg-primary text-primary-foreground rounded"
          onClick={() => setCount(count + 1)}
        >
          Increment
        </button>
        <p className="ml-4">Count: {count}</p>
      </div>
    </Layout>
  )
}

export default App
