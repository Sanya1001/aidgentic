"use client";
import * as React from "react"
 
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function Report(){
    return (
            <Card id="report-body">
                <CardHeader className="trans">
                    <CardTitle>Card Title</CardTitle>
                    <CardDescription>Card Description</CardDescription>
                </CardHeader>
                <CardContent className="trans">
                    <p>Card Content</p>
                </CardContent>
                <CardFooter className="trans">
                    <p>Card Footer</p>
                </CardFooter>
        </Card>
    );
}