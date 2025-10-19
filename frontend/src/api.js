import axios from 'axios';

const api = axios.create({
    baseURL: "https://task-setter.onrender.com"
});

export default api;