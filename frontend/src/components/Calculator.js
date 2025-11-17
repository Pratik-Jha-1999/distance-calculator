import { useState } from "react";

export default function Calculator({ setError }) {
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [unit, setUnit] = useState("miles");
  const [distance, setDistance] = useState("");

  const handleCalculate = async () => {
    setError("");
    setDistance("");

    if (!source || !destination) {
      setError("Please fill in both source and destination addresses.");
      return;
    }

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/distance?address1=${encodeURIComponent(
          source
        )}&address2=${encodeURIComponent(destination)}&unit=${encodeURIComponent(unit)}`, 
        {
        headers: {
          "X-API-Key": "Distance1234"
        }
        }
      );

      if (!res.ok) throw new Error("Calculation failed");
      const data = await res.json();
      setDistance(data.distance);
    } catch {
      setError("Something went wrong and the calculation failed.");
    }
  };

  return (
    <div className="main-box">
      <div className="form-grid">
        {/* Source */}
        <div className="input-group">
          <label>Source Address</label>
          <input
            value={source}
            onChange={(e) => setSource(e.target.value)}
            placeholder="Enter source address"
          />
        </div>

        {/* Destination */}
        <div className="input-group">
          <label>Destination Address</label>
          <input
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
            placeholder="Enter destination address"
          />
        </div>

        {/* Unit */}
        <div className="unit-group">
          <label>Unit</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                checked={unit === "miles"}
                onChange={() => setUnit("miles")}
              />
              Miles
            </label>
            <label>
              <input
                type="radio"
                checked={unit === "kilometers"}
                onChange={() => setUnit("kilometers")}
              />
              Kilometers
            </label>
            <label>
              <input
                type="radio"
                checked={unit === "both"}
                onChange={() => setUnit("both")}
              />
              Both
            </label>
          </div>
        </div>

        {/* Distance */}
        <div className="distance-display">
          <label>Distance</label>
          <div className="distance-value">{distance || "--"}</div>
        </div>
      </div>

      <button className="calculate-btn" onClick={handleCalculate}>
        <span>Calculate Distance</span> <span>🧮</span>
      </button>
    </div>
  );
}
