import React, { useEffect, useState } from "react";

function App() {

  const [status, setStatus] = useState("Loading...");
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:5000/")
      .then((res) => res.json())
      .then((data) => {
        setStatus(data.status);
      });

  }, []);

  const triggerAlert = async () => {

    const res = await fetch(
      "http://127.0.0.1:5000/trigger-alert"
    );

    const data = await res.json();

    setAlerts((prev) => [...prev, data.alert]);
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>🚀 Missile Detection Dashboard</h1>

      <h2>Status: {status}</h2>

      <button onClick={triggerAlert}>
        Trigger Emergency Alert
      </button>

      <h3>Threat Logs</h3>

      <ul>
        {alerts.map((alert, index) => (
          <li key={index}>{alert}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;