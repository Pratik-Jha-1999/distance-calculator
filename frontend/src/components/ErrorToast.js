
export default function ErrorToast({ message, onClose }) {
  return (
    <div className="error-toast">
      <div className="error-icon">⛔</div>
      <div className="error-text">
        <div className="error-title">Calculation failed</div>
        <p>{message}</p>
      </div>
      <button className="close-btn" onClick={onClose}>
        ✕
      </button>
    </div>
  );
}
