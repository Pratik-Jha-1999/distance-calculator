import { useState } from "react";
import "./App.css";
import Header from "./components/Header";
import Calculator from "./components/Calculator";
import HistoryTable from "./components/HistoryTable";
import ErrorToast from "./components/ErrorToast";


export default function App() {
  const [showHistory, setShowHistory] = useState(false);
  const [error, setError] = useState("");

  return (
    <div className="page-container">
      {/* Header */}
      <Header showHistory={showHistory} setShowHistory={setShowHistory} />

      {/* Conditional Pages */}
      {showHistory ? (
        <HistoryTable />
      ) : (
        <Calculator setError={setError} />
      )}

      {/* Error Toast */}
      {error && <ErrorToast message={error} onClose={() => setError("")} />}
    </div>
  );
}
