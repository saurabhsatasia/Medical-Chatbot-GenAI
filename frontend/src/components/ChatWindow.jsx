import React from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ChatMessage } from "./ChatMessage";
import { ChatInput } from "./ChatInput";
// import { LoadingDots } from "./LoadingDots";
import { Loader2 } from "lucide-react";

export function ChatWindow({ messages, onSendMessage, isLoading }) {
    return (
        <div className="flex flex-col">
            <ScrollArea className="h-[600px] mb-4">
                <div className="space-y-4 pr-4">
                    {messages.map((message) => (
                        <ChatMessage key={message.id} message={message} />
                    ))}
          
                    {isLoading && (
                        <div className="flex justify-start">
                            <div className="bg-muted rounded-lg p-3">
                                <Loader2 className="h-6 w-6 animate-spin text-primary" />
                            </div>
                        </div>
                    )}
                </div>
            </ScrollArea>

            <div className="pt-4 border-t">
                <ChatInput onSendMessage={onSendMessage} disabled={isLoading} />
                <p className="mt-2 text-xs text-muted-foreground text-center">
                    For informational purposes only. Consult a healthcare professional for medical advice.
                </p>
            </div>
        </div>
    );
  }