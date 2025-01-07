import React from "react";
import { Loader2 } from "lucide-react";
// import { Card, CardContent } from '@/components/ui/card';
import { cn } from "@/lib/utils";

export function ChatMessage({ message }) {
    const isBot = message.role === 'assistant';

    return (
        <div className={`flex ${isBot ? 'justify-start' : 'justify-end'} mb-4`}>
            <div className={cn(
                "rounded-lg p-3 max-w-[80%]",
                isBot ? "bg-gray-700 text-gray-100" : "bg-blue-600 text-white"
            )}>
                {isBot && (
                    <div className="flex items-center space-x-2 mb-1">
                        <span className="h-6 w-6 rounded-full bg-blue-600 flex items-center justify-center">
                            <span className="text-white text-sm">🤖</span>
                        </span>
                        <span className="font-medium text-gray-200">Medical Bot</span>
                    </div>
                )}

                <p>{message.content}</p>

                {isBot && message.sources && message.sources.length > 0 && (
                    <div className="mt-2 text-xs text-gray-400">
                        <p className="font-semibold">Sources:</p>
                        {message.sources.map((source, index) => (
                            <p key={index}>{source}</p>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}