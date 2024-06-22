import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

// Define the path to the JSON file
const dataFilePath = path.join(process.cwd(), 'data', 'submissions.json');

export async function POST(req: NextRequest) {
  try {
    // Parse the incoming request
    const newData = await req.json();

    // Read the existing data from the file
    let fileData: any[] = [];
    if (fs.existsSync(dataFilePath)) {
      const fileContent = fs.readFileSync(dataFilePath, 'utf-8');
      fileData = JSON.parse(fileContent);
    }

    // Append the new data
    fileData.push(newData);

    // Write the updated data back to the file
    fs.writeFileSync(dataFilePath, JSON.stringify(fileData, null, 2));

    return NextResponse.json({ message: 'Data saved successfully!' });
  } catch (error) {
    console.error('Error saving data:', error);
    return NextResponse.json({ message: 'Error saving data' }, { status: 500 });
  }
}
