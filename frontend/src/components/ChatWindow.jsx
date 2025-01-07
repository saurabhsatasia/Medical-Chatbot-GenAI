import React from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Card, CardContent } from "@/components/ui/card";
import { ChatMessage } from "./ChatMessage";
import { ChatInput } from "./ChatInput";
import { LoadingDots } from "./LoadingDots";

export function ChatWindow({ messages, onSendMessage, isLoading }) {
    return (
        <Card className="w-full max-w-2xl mx-auto h-[600px] flex flex-col">
            <ScrollArea className="flex-1 p-4">
                {messages.map((message) => (
                    <ChatMessage key={message.id} message={message} />
                ))}
                {isLoading && (
                    <div className='flex justify-center mb-4'>
                        <Card className='bg-muted'>
                            <CardContent className='p-4'>
                                <LoadingDots />
                            </CardContent>
                        </Card>

                    </div>
                )}
            </ScrollArea>
            <div className="p-4 border-t">
                <ChatInput onSendMessage={onSendMessage} disabled={isLoading} />
            </div>
        </Card>
    );
  }