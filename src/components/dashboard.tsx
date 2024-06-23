// pages/dashboard.tsx
import React from 'react';
import { NotifCard } from '@/components/notifcard';
import { CarouselSize } from './itemrow';
import { Report } from './report';

const Dashboard: React.FC = () => {
  return (
    <div className="min-h-screen flex" id='dash'>
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-white flex flex-col" id='sidebar'>
        {/* <div className="p-4 text-center text-xl font-semibold">
          Dashboard
        </div> */}
        <nav className="flex-1 p-4">
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 sidebar-item">
            Overview
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 sidebar-item">
            Reports
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 sidebar-item">
            Analytics
          </a>
          <a href="#" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 sidebar-item">
            Settings
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">

        {/* Content */}
        <main className="flex-1 p-4" id='resource-content'>
          <div className="container mx-auto">
            <div className="bg-white p-6 rounded shadow" id='resource-main'>
              <h2 className="text-2xl font-semibold mb-4">Dashboard</h2>
              <p>Welcome Sanya, your organization has a call to respond to the ongoing wildfire crisis in New Mexico, California.</p>
            </div>
          </div>
          <div className="p-6 rounded shadow" id='resource-car'>
            <CarouselSize />
          </div>
          <div className="p-6 rounded shadow" id='third-row'>
            <div className="p-6 rounded shadow" id='notifs'>
              <NotifCard />
            </div>
            <div className="p-6 rounded shadow" id='report-card'>
              <Report />
            </div>
          </div>
            
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
