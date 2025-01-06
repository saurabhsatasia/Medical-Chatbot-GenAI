import React from "react";

export function Layout({ children }) {
    return (
        <div className="min-h-screen bg-background p-8">
            <header className="mb-8 text-center">
                <div className="max-w-2xl mx-auto">
                    <h1 className="text-2xl font-semibold">Medical Chatbot</h1>
                    <p className="text-muted-foreground">Ask me anything about medical topics</p>
                </div>
            </header>
            <main className="flex-1">
                <div className="max-w-2xl mx-auto p-4">{children}</div>
            </main>
        </div>
    )
}