import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [domain, setDomain] = useState("");
  const [result, setResult] = useState("");

  const createCourse = async () => {
    const res = await axios.post("http://localhost:8000/create_course", null, {
      params: { domain }
    });
    setResult(JSON.stringify(res.data, null, 2));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Course Factory</h1>
      <input value={domain} onChange={e => setDomain(e.target.value)} />
      <button onClick={createCourse}>Create Course</button>
      <pre>{result}</pre>
    </div>
  );
}
