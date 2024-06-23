import Image from "next/image";
import Navbar from "@/components/navbar";

export default function Home() {
  return (
    <div>
      <main className="flex w-full min-h-screen flex-col items-center justify-between">
      <div
        className="min-h-screen bg-cover bg-center flex items-center" id="home"
      >
      <div className="absolute inset-0 bg-black opacity-50"></div>
      {/* <video
        autoPlay
        loop
        muted
        className="absolute inset-0 w-full h-full object-cover"
      >
        <source src="/videos/background-video.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video> */}
      <div className="container mx-auto text-center z-10" id="landing">
        <h1 className="text-5xl font-bold text-white mb-8 acme-regular">Welcome, Siddhartha</h1>
        <p className="text-lg text-white pt-mono-regular">There is an ACTIVE wildfire situation in New Mexico, California</p>
      </div>
    </div>
    </main>
    <Navbar />
    </div>
   
  );
}
