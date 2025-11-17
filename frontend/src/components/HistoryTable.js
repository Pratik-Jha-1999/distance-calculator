import { useEffect, useState } from "react";

export default function HistoryTable() {
  const [data, setData] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // 👇 Function to fetch historical records
  const handleViewHistory = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch("http://127.0.0.1:8000/history", {
        headers: {
          "X-API-Key": "Distance1234"
        }
      });
      if (!response.ok) {
        throw new Error("Failed to fetch history data");
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      console.error("Error fetching history:", err);
      setError("Failed to load history data.");
    } finally {
      setLoading(false);
    }
  };

  // 👇 Fetch data automatically when component mounts
  useEffect(() => {
    handleViewHistory();
  }, []);

  return (
    <div className="history-section">
      <h2 className="section-title">Historical Queries</h2>
      <p className="section-subtitle">History of the user's queries.</p>

      {loading && <p>Loading history...</p>}
      {error && <p className="error-message">{error}</p>}

      {!loading && !error && (
        <div className="table-container">
          <table className="history-table">
            <thead>
              <tr>
                <th>Source Address</th>
                <th>Destination Address</th>
                <th>Distance in Miles</th>
                <th>Distance in Kilometers</th>
              </tr>
            </thead>
            <tbody>
              {data.length > 0 ? (
                data.map((item, i) => (
                  <tr key={i}>
                    <td>{item.source_address}</td>
                    <td>{item.destination_address}</td>
                    <td>{item.distance_in_miles}</td>
                    <td>{item.distance_in_kilometers}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" style={{ textAlign: "center" }}>
                    No records found
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
