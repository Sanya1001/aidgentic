// pages/dashboard.tsx
import React from 'react';

const Dashboard: React.FC = () => {
  return (
    <div className="min-h-screen flex">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-white flex flex-col">
        <div className="p-4 text-center text-xl font-semibold">
          Dashboard
        </div>
        <nav className="flex-1 p-4">
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700">
            Overview
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700">
            Reports
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700">
            Analytics
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700">
            Settings
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        {/* Top Navigation */}
        <header className="bg-gray-100 text-gray-800 p-4 shadow">
          <div className="container mx-auto flex justify-between">
            <div className="font-semibold">Welcome to the Dashboard</div>
            <div>
              <button className="py-2 px-4 bg-gray-800 text-white rounded">Logout</button>
            </div>
          </div>
        </header>

        {/* Content */}
        <main className="flex-1 bg-gray-200 p-4">
          <div className="container mx-auto">
            <div className="bg-white p-6 rounded shadow">
              <h2 className="text-2xl font-semibold mb-4">Dashboard Content</h2>
              <p>This is where your dashboard content will go.</p>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
