import { useState } from 'react'

export default function Topbar() {
    return (
        <div className="bg-red-500 text-white p-4 flex justify-between items-center">
            <div className="text-lg font-bold">
                <img src="/nintendo.png" 
                    alt="Nintendo" 
                    className='h-6 inline-block mr-2'
                    />
            </div>
            <div className="flex space-x-4">
                <a href="#" className="hover:text-gray-400">Home</a>
                <a href="#" className="hover:text-gray-400">About</a>
                <a href="#" className="hover:text-gray-400">Contact</a>
            </div>
        </div>
    )
}