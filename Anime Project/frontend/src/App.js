// src/App.js
import React, { useState } from 'react';
import Spinner from './components/spinner';
import AnimeList from './components/animeList';
import fetchAnimeData from './api/fetchAnimeData';
import './App.css';

const App = () => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState([]);
  const [mood, setMood] = useState('Happy'); // Default mood
  const handleFetchData = async () => {
    setLoading(true);
    try {
      const animeData = await fetchAnimeData(mood);
      setData(animeData);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };



  return (
    <div className="App">
      <h1>Anime List</h1>
      <div class="select_con">
        <label htmlFor="mood">Select Mood:</label>
        <select id="mood" value={mood} onChange={(e) => setMood(e.target.value)}>
          <option value="Happy">Happy</option>
          <option value="Sad">Sad</option>
          <option value="Scared">Scared</option>
          <option value="Bored">Bored</option>
          <option value="Relaxed">Relaxed</option>
          <option value="Inspired">Inspired</option>
          <option value="Confused">Confused</option>
        </select>
            <button onClick={handleFetchData} class="glass-button">create list</button>
      </div>
      {loading ? <Spinner /> : <AnimeList data={data} />}
    </div>
  );
};

export default App;
