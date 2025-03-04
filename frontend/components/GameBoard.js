import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Text, Button, ActivityIndicator } from 'react-native-paper';
import HealthBar from './HealthBar';
import Room from './Room';
import Weapon from './Weapon';
import Deck from './Deck';

const GameBoard = ({ 
  gameState, 
  loading, 
  onSelectCard, 
  onAvoidRoom,
  onNewGame
}) => {
  if (!gameState) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#1e2a3d" />
        <Text>Loading game...</Text>
      </View>
    );
  }

  // Check if game is over
  const isGameOver = gameState.health <= 0 || (gameState.cards_remaining === 0 && gameState.current_room.length <= 1);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {/* Health Bar */}
      <HealthBar health={gameState.health} maxHealth={20} />
      
      {/* Deck Status */}
      <View style={styles.deckStatus}>
        <Deck cardsRemaining={gameState.cards_remaining} />
      </View>
      
      {/* Equipped Weapon */}
      <Weapon 
        weapon={gameState.equipped_weapon} 
        monsters={gameState.slain_monsters} 
      />
      
      {/* Current Room */}
      <View style={styles.roomContainer}>
        <Text style={styles.sectionTitle}>Current Room</Text>
        <Room 
          cards={gameState.current_room} 
          onSelectCard={onSelectCard}
          disabled={loading || isGameOver} 
        />
      </View>
      
      {/* Game Actions */}
      <View style={styles.actionsContainer}>
        <Button 
          mode="contained" 
          onPress={onAvoidRoom}
          disabled={loading || isGameOver || gameState.avoided_previous_room || gameState.current_room.length < 4}
          style={styles.button}
        >
          Avoid Room
        </Button>
        
        {/* Display if game is over */}
        {isGameOver && (
          <View style={styles.gameOverContainer}>
            <Text style={styles.gameOverText}>
              {gameState.health <= 0 ? 'You have been defeated!' : 'You survived the dungeon!'}
            </Text>
            <Text style={styles.scoreText}>
              Final Score: {gameState.score}
            </Text>
            <Button 
              mode="contained" 
              onPress={onNewGame}
              style={[styles.button, styles.newGameButton]}
            >
              New Game
            </Button>
          </View>
        )}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  roomContainer: {
    marginVertical: 16,
  },
  actionsContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
  button: {
    marginVertical: 8,
    width: '80%',
    borderRadius: 8,
    backgroundColor: '#1e2a3d',
  },
  deckStatus: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginVertical: 10,
  },
  gameOverContainer: {
    marginTop: 20,
    padding: 20,
    borderRadius: 10,
    backgroundColor: 'rgba(0,0,0,0.05)',
    width: '100%',
    alignItems: 'center',
  },
  gameOverText: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  scoreText: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#1e2a3d',
  },
  newGameButton: {
    backgroundColor: '#388e3c',
    marginTop: 10,
  }
});

export default GameBoard;