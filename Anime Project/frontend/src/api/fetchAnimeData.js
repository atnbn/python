import axios from 'axios';

const fetchAnimeData = async (mood) => {
    try {
        const response = await axios.get(`http://localhost:5000/api/anime?mood=${mood}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching anime data:', error);
        throw error;
    }
};

export default fetchAnimeData;
