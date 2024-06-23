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
    ngo_id: string;
    timestamp: string;
    report: string;
  }

export function Report(){

    const [report, setReport] = useState<Report | null>(null);
    const id = "1";

    useEffect(() => {
        fetch('/api/reports')
        .then((response) => response.json())
        .then((data) => {
            const matchingReport = data.message.find((report: Report) => report.ngo_id == id);
            setReport(matchingReport || null);
          })
        .catch((error) => console.error('Error fetching reports:', error));
    }, []);

    return (
        <div>
            <Card id="report-body">
                <CardHeader>
                    <CardTitle>{report?.ngo_id}</CardTitle>
                    <CardDescription>{report?.timestamp}</CardDescription>
                </CardHeader>
                <CardContent>
                    <p>{report?.report}</p>
                </CardContent>
                <CardFooter>
                    <p>Card Footer</p>
                </CardFooter>
            </Card>
        </div>
        
    );
}