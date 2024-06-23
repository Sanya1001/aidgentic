"use client";

import React, { useState } from "react";
import Navbar from "../../components/navbar";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { timeStamp } from "console";

const FormPage: React.FC = () => {
  const [formData, setFormData] = useState({
    city: "",
    state: "",
    name: "",
    topic: "",
    description: "",
    peopleAffected: "",
  });

  const handleChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >
  ) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // console.log('Form Data Submitted:', formData);


    const currentTimestamp = Date.now();
    console.log(currentTimestamp); // Output: current timestamp in milliseconds
    const currentDate = new Date();
    const formattedDate = currentDate.toLocaleString();
    console.log(formattedDate); // Output: formatted date and time
    const dataWithTimestamp = { ...formData, timestamp: formattedDate };

    try {
      const response = await fetch("/api/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dataWithTimestamp),
      });

      const result = await response.json();
      console.log("Form Data Submitted:", result);

      // Reset form fields after submission
      setFormData({
        city: "",
        state: "",
        name: "",
        topic: "",
        description: "",
        peopleAffected: "",
      });

      alert("Data saved successfully!");
    } catch (error) {
      console.error("Error submitting form data:", error);
      alert("Error submitting data.");
    }
  };

  return (
    <div id="reports">
      <div className="w-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md w-full space-y-12" id="report">
          <div>
            <h2 className="mt-6 text-center text-3xl font-extrabold text-white">
              Report a situation
            </h2>
          </div>
          <form
            className="mt-8 space-y-12 max-w-md w-full"
            onSubmit={handleSubmit}
          >
            <div className="rounded-md shadow-sm -space-y-px">
              <div className="space-y-4">
                <label htmlFor="location" className="sr-only">
                  City
                </label>
                <input
                  id="city"
                  name="city"
                  type="text"
                  autoComplete="city"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                  placeholder="City"
                  value={formData.city}
                  onChange={handleChange}
                />
              </div>
              <div className="space-y-4">
                <label htmlFor="location" className="sr-only">
                  State
                </label>
                <input
                  id="state"
                  name="state"
                  type="text"
                  autoComplete="state"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                  placeholder="State"
                  value={formData.state}
                  onChange={handleChange}
                />
              </div>
              <div className="space-y-4">
                <label htmlFor="name" className="sr-only">
                  Name
                </label>
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
                <label htmlFor="topic" className="sr-only">
                  Topic
                </label>
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
                <label htmlFor="description" className="sr-only">
                  Description
                </label>
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
                <label htmlFor="peopleAffected" className="sr-only">
                  People Affected
                </label>
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

      <Accordion type="single" collapsible className="w-full accord" id="reports-accord">
        <AccordionItem value="item-1">
          <AccordionTrigger className="reports-accord">
            [ONGOING] Report from California Office of the Governor
          </AccordionTrigger>
          <AccordionContent className="accord-content">
          SACRAMENTO – As hot, dry conditions and strong winds continue to propel dangerous wildfire conditions across the West, Governor Gavin Newsom today announced the deployment of fire and rescue personnel to New Mexico to aid in human remains detection coordination and recovery efforts.

In close coordination with the Federal Emergency Management Agency (FEMA), Governor Newsom directed his Office of Emergency Services (Cal OES) to immediately deploy five firefighters from California’s Urban Search and Rescue (US&R) Task Forces’ Incident Support Team along with 11 Human Remains Detection dogs and their handlers.

“California is all too familiar with the devastating impacts of major wildfires on our communities,” said Nancy Ward, Director of Cal OES. “California stands ready to continue to support our neighbors to the East with specialized personnel and recovery experts, while maintaining the capacity to keep Californians safe as we head into peak wildfire season.”

The Incident Support Team provides a group of highly qualified specialists to provide local officials with technical assistance, management and coordination of US&R resources.

The specialized team members deployed to New Mexico come from California-based US&R Task Forces, including local government fire and rescue personnel from Oakland, Orange County, Roseville and San Diego fire departments. The California-based US&R Canine Search Teams come from Los Angeles City, Los Angeles County, Orange County and Riverside City fire departments.

This deployment builds on California’s far-reaching efforts to aid other states during emergencies. Last year, California deployed Urban Search and Rescue members to Hawaii to support wildfire response. In 2022, California deployed firefighters, disaster recovery experts, and other personnel to Oregon, New Mexico, and Montana. In 2021, California sent fire engines to assist Oregon’s response to the Bootleg Fire and Specialized Urban Search and Rescue Resources teams to Florida following the Surfside condo collapse.
 <br></br>
 Read more <a href="https://news.caloes.ca.gov/governor-gavin-newsom-deploys-fire-and-rescue-personnel-to-south-fork-and-salt-fires-in-new-mexico/">
  here
 </a>
          </AccordionContent>
        </AccordionItem>
        <AccordionItem value="item-2">
          <AccordionTrigger className="reports-accord">
            Report from citizen about wildfire sighting
          </AccordionTrigger>
          <AccordionContent className="accord-content">
            Yes. It comes with default styles that matches the other
            components&apos; aesthetic.
          </AccordionContent>
        </AccordionItem>
        <AccordionItem value="item-3">
          <AccordionTrigger className="reports-accord">
            Report from volunteer organization about air quality
          </AccordionTrigger>
          <AccordionContent className="accord-content">
            Yes. It&apos;s animated by default, but you can disable it if you
            prefer.
          </AccordionContent>
        </AccordionItem>
      </Accordion>
      <Navbar />
    </div>
  );
};

export default FormPage;
