import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

interface Report {
    ngo_id: string;
    timestamp: string;
    report: string;
  }

// Define the path to the JSON file
const dataFilePath = path.join(process.cwd(), 'data', 'notifications.json');

export async function GET(req: NextRequest) {
  try {
    // Read the existing data from the file
    let fileData: Report[] = [];
    if (fs.existsSync(dataFilePath)) {
      const fileContent = fs.readFileSync(dataFilePath, 'utf-8');
      fileData = JSON.parse(fileContent);
    }

    return NextResponse.json({ message: fileData });
  } catch (error) {
    console.error('Error saving data:', error);
    return NextResponse.json({ message: 'Error saving data' }, { status: 500 });
  }
}