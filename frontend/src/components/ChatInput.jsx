import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export function ChatInput({ onSendMessage, disabled }) {
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (message.trim()) {
            onSendMessage(message);
            setMessage('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex space-x-2">
            <Input
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your medical question..."
                disabled={disabled}
                className="flex-1"
            />
            <Button 
                type="submit" 
                disabled={disabled || !message.trim()}
                className="bg-blue-600 hover:bg-blue-700">Send</Button>
        </form>
        );
    }