import React from 'react';
import'./animelist.css'
const AnimeList = ({ data }) => (
    <div className="anime-list">
        {data.map((anime) => (
            <div key={anime.id} className="anime-item" >
                <h3>{anime.title}</h3>
                <img src={anime.image_url} alt={anime.title} />
                <p>Episodes: {anime.episodes}</p>
                <p>Year: {anime.year}</p>
                <p>Genres: {anime.genres.join(', ')}</p>
            </div>
        ))}
    </div>
);

export default AnimeList;