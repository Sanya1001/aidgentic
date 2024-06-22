"use client";

import React, { useState } from 'react';
import Navbar from '../../components/navbar';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"


const FormPage: React.FC = () => {
  const [formData, setFormData] = useState({
    location: '',
    name: '',
    topic: '',
    description: '',
    peopleAffected: ''
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // console.log('Form Data Submitted:', formData);

    try {
      const response = await fetch('/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      const result = await response.json();
      console.log('Form Data Submitted:', result);

      // Reset form fields after submission
      setFormData({
        location: '',
        name: '',
        topic: '',
        description: '',
        peopleAffected: ''
      });

      alert('Data saved successfully!');
    } catch (error) {
      console.error('Error submitting form data:', error);
      alert('Error submitting data.');
    }
  };

  return ( 
    <div>
    <div className="min-h-screen w-full flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      
      <div className="max-w-md w-full space-y-12">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Submit Information</h2>
        </div>
        <form className="mt-8 space-y-12 max-w-md w-full" onSubmit={handleSubmit}>
          <div className="rounded-md shadow-sm -space-y-px">
            <div className="space-y-4">
              <label htmlFor="location" className="sr-only">Location</label>
              <input
                id="location"
                name="location"
                type="text"
                autoComplete="location"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Location"
                value={formData.location}
                onChange={handleChange}
              />
            </div>
            <div className="space-y-4">
              <label htmlFor="name" className="sr-only">Name</label>
              <input
                id="name"
                name="name"
                type="text"
                autoComplete="name"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Name"
                value={formData.name}
                onChange={handleChange}
              />
            </div>
            <div className="space-y-4">
              <label htmlFor="topic" className="sr-only">Topic</label>
              <input
                id="topic"
                name="topic"
                type="text"
                autoComplete="topic"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Topic"
                value={formData.topic}
                onChange={handleChange}
              />
            </div>
            <div className="space-y-4">
              <label htmlFor="description" className="sr-only">Description</label>
              <textarea
                id="description"
                name="description"
                autoComplete="description"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Description"
                value={formData.description}
                onChange={handleChange}
              />
            </div>
            <div className="space-y-4">
              <label htmlFor="peopleAffected" className="sr-only">People Affected</label>
              <input
                id="peopleAffected"
                name="peopleAffected"
                type="text"
                autoComplete="people-affected"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="People Affected"
                value={formData.peopleAffected}
                onChange={handleChange}
              />
            </div>
          </div>
          <div className="space-y-4">
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
    </div>
  );
};

export default FormPage;
