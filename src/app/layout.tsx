import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Head from 'next/head';
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "aidgentic",
  description: "Respond to humanitarian crises with aidgentic",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com"/>
        <link href="https://fonts.googleapis.com/css2?family=Acme&display=swap" rel="stylesheet"/>
        <link href="https://fonts.googleapis.com/css2?family=Acme&family=PT+Mono&display=swap" rel="stylesheet"/>
      </Head>
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
