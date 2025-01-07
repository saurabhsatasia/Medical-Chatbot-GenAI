import React from "react";
import { Card, CardContent } from '@/components/ui/card';
import { cn } from '@/lib/utils';

export function ChatMessage({ message }) {
    return (
        <div className={cn(
            "felx gap-3 mb-4", message.role === "user" ? "justify-end" : "justify-start"
        )}>
            <Card className={cn(
                'max-w-[80%]', message.role === "user" ? "bg-primary text-primary-foreground" : "bg-muted"
            )}>
                <CardContent className='p-3'>
                    <p>{message.content}</p>
                    {message.sources && message.sources.length > 0 && (
                        <div className="mt-2 text-sm opacity-80">
                            <p className="font-semibold">Sources:</p>
                            {message.sources.map((source, index) => (
                                <p key={index} className="text-xs">{source}</p>
                            ))}
                        </div>
                    )}
                </CardContent>
            </Card>
        </div>
    );
}