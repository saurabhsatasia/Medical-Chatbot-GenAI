import { useState } from 'react';
import { Layout } from './components/Layout';
import { ChatWindow } from './components/ChatWindow';
import { sendMessage } from './api';

function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (content) => {
    if (!content.trim()) return;

    const userMessage = {
      id: Date.now().toString(),
      content,
      role: 'user'
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await sendMessage(content);
      
      if (response && response.answer) {
        const assistantMessage = {
          id: (Date.now() + 1).toString(),
          content: response.answer,
          role: 'assistant',
          sources: response.sources || []
        };
        setMessages(prev => [...prev, assistantMessage]);
      } else {
        throw new Error('Invalid response format');
      }
    } catch (error) {
      console.error('Error details:', error);
      
      const errorMessage = {
        id: (Date.now() + 1).toString(),
        content: error.message || 'An error occurred while processing your request.',
        role: 'assistant'
      };
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <ChatWindow
        messages={messages}
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
      />
    </Layout>
  );
}

export default App;
