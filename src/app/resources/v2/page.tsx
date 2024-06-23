"use client";

import React, { useState } from 'react';
import Navbar from '../../../components/navbar';
import Dashboard from '@/components/dashboard';
import Dashboard2 from '@/components/dashboard2';

const ResourcesPage: React.FC = () => {
    return(
        <div id='outer-resources'>
        <div id="resources">
            <Dashboard2 />
            <Navbar />
        </div>
        </div>
    );
};

export default ResourcesPage;