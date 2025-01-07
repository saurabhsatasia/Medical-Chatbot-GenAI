import React from "react";
import { cn } from "@/lib/utils";

export function LoadingDots({ className }) {
    return (
        <div className={cn("flex space-x-1", className)}>
            <div className="w-2 h-2 bg-current rounded-full animate-bounce" />
            <div className="w-2 h-2 bg-current rounded-full animate-bounce [animation-delay:0.2s]" />
            <div className="w-2 h-2 bg-current rounded-full animate-bounce [animation-delay:0.4s]" />
        </div>
    )
}