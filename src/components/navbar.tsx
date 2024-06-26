"use client"
import React from 'react';
import Link from 'next/link';

export default function Navbar () {
  return (
    <div className="z-20">
      <nav className="bg-gray-800 p-4" id='navbar'>
      <div className="max-w-7xl mx-auto z-10">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <span className="text-white text-lg font-semibold">sync</span>
          </div>
          <div className="flex space-x-4">
            <a
              href="/"
              className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
            >
              Dashboard
            </a>
            <a
              href="#"
              className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
            >
              Notifications
            </a>
            <a
              href="/form"
              className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
            >
              Reports
            </a>
            <a
              href="/resources"
              className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
            >
              Resources
            </a>
          </div>
        </div>
      </div>
    </nav>
    </div>

  );
};

// export default Navbar;
