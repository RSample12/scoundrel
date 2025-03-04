import React, { createContext, useState, useContext, useEffect } from 'react';
import { createGame, performAction } from '../services/api';
import AsyncStorage from '@react-native-async-storage/async-storage';

const GameContext = createContext();

export const useGame = () => useContext(GameContext);

export const GameProvider = ({ children }) => {
  const [gameState, setGameState] = useState(null);
  const [gameId, setGameId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load saved game state
  useEffect(() => {
    const loadSavedState = async () => {
      try {
        const savedState = await AsyncStorage.getItem('gameState');
        const savedId = await AsyncStorage.getItem('gameId');
        if (savedState && savedId) {
          setGameState(JSON.parse(savedState));
          setGameId(savedId);
        }
      } catch (err) {
        console.error('Failed to load saved game:', err);
      }
    };
    loadSavedState();
  }, []);

  // Save game state when it changes
  useEffect(() => {
    const saveState = async () => {
      if (gameState && gameId) {
        try {
          await AsyncStorage.setItem('gameState', JSON.stringify(gameState));
          await AsyncStorage.setItem('gameId', gameId);
        } catch (err) {
          console.error('Failed to save game:', err);
        }
      }
    };
    saveState();
  }, [gameState, gameId]);

  const startNewGame = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await createGame();
      setGameId(response.game_id);
      setGameState(response.state);
    } catch (err) {
      setError('Failed to start game. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const selectCard = async (cardIndex) => {
    try {
      setLoading(true);
      setError(null);
      const response = await performAction(gameId, 'select_card', cardIndex);
      setGameState(response.state);
    } catch (err) {
      setError('Failed to select card. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const avoidRoom = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await performAction(gameId, 'avoid_room');
      setGameState(response.state);
    } catch (err) {
      setError('Failed to avoid room. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <GameContext.Provider
      value={{
        gameState,
        loading,
        error,
        startNewGame,
        selectCard,
        avoidRoom,
      }}
    >
      {children}
    </GameContext.Provider>
  );
};