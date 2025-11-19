import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts API:', apiUrl);
        console.log('Fetched workouts:', results);
      });
  }, [apiUrl]);

  return (
    <div>
      <h2 className="mb-4 text-primary">Workouts</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered table-hover align-middle">
          <thead className="table-dark">
            <tr>
              <th>Name</th>
              <th>Difficulty</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={idx}>
                <td>{workout.name}</td>
                <td>{workout.difficulty}</td>
                <td>{workout.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
