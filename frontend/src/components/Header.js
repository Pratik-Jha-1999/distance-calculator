
export default function Header({ showHistory, setShowHistory }) {
  return (
    <div className="header">
      <div>
        <h1 className="title">Distance Calculator</h1>
        <p className="subtitle">
          Prototype web application for calculating the distance between addresses.
        </p>
      </div>

      {showHistory ? (
        <button className="history-btn" onClick={() => setShowHistory(false)}>
          Back to Calculator ▣
        </button>
      ) : (
        <button className="history-btn" onClick={() => setShowHistory(true)}>
          View Historical Queries ↻
        </button>
      )}
    </div>
  );
}
