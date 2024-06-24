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
import dotenv  from 'dotenv';

dotenv.config();

interface Report {
    title: string;
    ngo_name: string;
    resources: string;
    timestamp: string;
    report: string;
  }


const SERVER_IP = '0.0.0.0:8000';
const ngo_name = process.env.NGO_NAME || "Florida Humane Society";

export function Report(){

    const [report, setReport] = useState<Report | null>(null);

    useEffect(() => {
        fetch(`http://${SERVER_IP}/notifications`).then(async res => {
            const data = (await res.json()) as Report[];
            const matchingReport = data.reverse().find((report: Report) => report.ngo_name == ngo_name);
            setReport(matchingReport || null);}
        )}, [])

    return (
        <div>
            <Card id="report-body">
                <CardHeader>
                    <CardTitle>{report?.title || "No reports right now"}</CardTitle>
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