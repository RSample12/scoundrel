import axios from 'axios';

// Replace with your actual backend URL when deployed
// For local testing with Expo Go, use your computer's IP address 
const API_URL = 'http://192.168.1.149:8000';

// Configure axios with some defaults
const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 10000, // 10 seconds
  headers: {
    'Content-Type': 'application/json',
  }
});

export const createGame = async () => {
  try {
    const response = await apiClient.post('/new-game');
    return response.data;
  } catch (error) {
    console.error('API Error - Create Game:', error);
    throw error;
  }
};

export const performAction = async (gameId, actionType, cardIndex = null) => {
  try {
    const payload = {
      game_id: gameId,
      action_type: actionType,
    };
    
    // Only include card_index if it's provided
    if (cardIndex !== null) {
      payload.card_index = cardIndex;
    }
    
    const response = await apiClient.post('/action', payload);
    return response.data;
  } catch (error) {
    console.error(`API Error - ${actionType}:`, error);
    throw error;
  }
};