export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center font-sans">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
      <p className="mt-4 text-lg text-gray-600">
        Get started by editing <code className="bg-gray-100 p-1 rounded">app/page.tsx</code>
      </p>
      <video id="webcam" className="mt-6 w-1/2 h-128 bg-white"></video>
    </div>
  );
}
