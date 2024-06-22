import Image from "next/image";

export default function Home() {
  return (
    <main className="flex w-full min-h-screen flex-col items-center justify-between p-24">
    <div
      className="min-h-screen bg-cover bg-center flex items-center" id="home"
    >
      <div className="container mx-auto text-center" id="landing">
        <h1 className="text-5xl font-bold text-white mb-8">Welcome to Your Dashboard</h1>
        <p className="text-lg text-white">If you see something, say something</p>
      </div>
    </div>
    </main>
  );
}
