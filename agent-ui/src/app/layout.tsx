import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Document Converter",
  description: "AI-powered document conversion assistant",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}