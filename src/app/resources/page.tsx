"use client";

import React, { useState } from 'react';
import Navbar from '../../components/navbar';
import Dashboard from '@/components/dashboard';

const ResourcesPage: React.FC = () => {
    return(
        <div id='outer-resources'>
        <div id="resources">
            <Dashboard />
            <Navbar />
        </div>
        </div>
    );
};

export default ResourcesPage;