"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

export default function Home() {
  return (
    <CopilotKit runtimeUrl="http://localhost:7777/agui">
      <div style={{ height: "100vh" }}>
        <CopilotChat
          labels={{
            title: "Document Converter",
            initial: "Upload a document and choose an output format: markdown, JSON, HTML, text, or doctags.",
          }}
        />
      </div>
    </CopilotKit>
  );
}