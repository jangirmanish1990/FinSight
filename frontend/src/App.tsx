import React from "react";

export default function App() {
  return (
    <div className="min-h-screen bg-navy font-ui text-white flex items-center justify-center">
      <div className="text-center">
        {/* Logo mark */}
        <div className="mx-auto mb-6 w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan to-purple flex items-center justify-center">
          <span className="font-display text-3xl text-black font-bold">F</span>
        </div>

        <h1 className="font-display text-5xl text-white mb-2">FinSight AI</h1>
        <p className="text-cyan text-lg mb-1">Autonomous Financial Research Agent</p>
        <p className="text-muted text-sm font-mono mb-8">Day 1 scaffold — v0.1.0</p>

        {/* Status card */}
        <div className="inline-flex flex-col gap-3 bg-navy-light border border-border rounded-xl p-6 text-left min-w-72">
          <StatusRow label="React + Vite"    status="ok" />
          <StatusRow label="Tailwind CSS"    status="ok" />
          <StatusRow label="Font system"     status="ok" />
          <StatusRow label="FastAPI backend" status="pending" />
          <StatusRow label="LangGraph agents" status="pending" />
        </div>

        <p className="mt-8 text-dim text-xs font-mono">
          run <span className="text-cyan">make dev-backend</span> in another terminal to start FastAPI
        </p>
      </div>
    </div>
  );
}

function StatusRow({ label, status }: { label: string; status: "ok" | "pending" | "error" }) {
  const dot: Record<string, string> = {
    ok:      "bg-teal",
    pending: "bg-amber opacity-60",
    error:   "bg-coral",
  };
  const text: Record<string, string> = {
    ok:      "text-teal",
    pending: "text-amber",
    error:   "text-coral",
  };
  return (
    <div className="flex items-center justify-between gap-8">
      <span className="text-muted text-sm">{label}</span>
      <div className="flex items-center gap-2">
        <span className={`w-2 h-2 rounded-full ${dot[status]}`} />
        <span className={`text-xs font-mono font-medium ${text[status]}`}>
          {status.toUpperCase()}
        </span>
      </div>
    </div>
  );
}
