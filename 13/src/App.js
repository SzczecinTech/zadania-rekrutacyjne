import React, { useState, useEffect } from 'react';
import './App.css';

const Description = ({id}) => {
  const [plot, setPlot] = useState('laoding');
  useEffect(() => {
    fetch(`http://www.omdbapi.com/?i=${id}&apikey=PlzBanMe`)
      .then(response => response.json())
      .then(movie => {
        setPlot(movie.Plot);
      });
  }, [])
  return (
    <div>
      {plot}
    </div>
  );
}

function App() {
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch('http://www.omdbapi.com/?s=robot&apikey=PlzBanMe')
      .then(response => response.json())
      .then(data => {
        setMovies(data.Search)
      });
  }, []);
  return (
    <div className="App">
      {movies.map(movie => (
        <div>
          <h2>{movie.Title} ({movie.Year}) ({movie.Type})</h2>
          <Description
            id={movie.imdbID}
          />
        </div>
      ))}
    </div>
  );
}

export default App;
