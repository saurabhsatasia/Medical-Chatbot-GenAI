import React from "react";

export function Layout({ children }) {
    return (
        <div className="min-h-screen w-full bg-[#0F1218] flex">
            <div className="flex-1 flex flex-col">
                <div className="text-center py-8">
                    <h1 className="text-4xl font-bold text-white mb-2">
                        Medical Chatbot
                    </h1>
                    <p className="text-gray-600 dark:text-gray-300">
                        Your AI-powered medical information assistant
                    </p>
                </div>
                <div className="flex-1 flex items-center justify-center px-4">
                    <div className="w-full max-w-2xl">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    )
}