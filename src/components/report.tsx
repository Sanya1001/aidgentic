"use client";
import * as React from "react"
import { useEffect, useState } from 'react';
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { get } from "http";
import { time } from "console";

interface Report {
    title: string;
    ngo_name: string;
    resources: string;
    timestamp: string;
    report: string;
  }

export function Report(){

    const [report, setReport] = useState<Report | null>(null);
    const id = "California Fire Foundation";

    useEffect(() => {
        fetch('/api/reports')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            const matchingReport = data.message.reverse().find((report: Report) => report.ngo_name == id);
            setReport(matchingReport || null);
          })
        .catch((error) => console.error('Error fetching reports:', error));
    }, []);

    return (
        <div>
            <Card id="report-body">
                <CardHeader>
                    <CardTitle>{report?.title}</CardTitle>
                    <CardDescription>{report?.timestamp}</CardDescription>
                </CardHeader>
                <CardContent>
                    {report?.report.split('\n').map((line, index) => (
                        <p key={index}>{line} <br /></p>
                ))}
                </CardContent>
                <CardFooter>
                    <p>{report?.ngo_name}</p>
                </CardFooter>
            </Card>
        </div>

    );
}