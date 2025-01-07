import { useState } from 'react';
import { Layout } from './components/Layout';
import { ChatWindow } from './components/ChatWindow';
import { sendMessage } from './api';
import { ThemeProvider } from './components/theme-provider';
import { ThemeToggle } from './components/ThemeToggle';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

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
    <ThemeProvider>
      <div className="min-h-screen bg-background">
        <div className="container mx-auto p-6">
          <Card className="w-full max-w-4xl mx-auto">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-4">
              <div>
                <CardTitle className="text-2xl font-bold">Medical Chatbot</CardTitle>
                <p className="text-sm text-muted-foreground">
                  Your AI-powered medical information assistant
                </p>
              </div>
              <ThemeToggle />
            </CardHeader>
            <CardContent>
              <ChatWindow
                messages={messages}
                onSendMessage={handleSendMessage}
                isLoading={isLoading}
              />
            </CardContent>
          </Card>
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
