import React, { useEffect } from 'react';
import { View, StyleSheet, ScrollView, Alert } from 'react-native';
import { Text, Button, ActivityIndicator } from 'react-native-paper';
import { useGame } from '../contexts/GameContext';
import Room from '../components/Room';
import HealthBar from '../components/HealthBar';
import Weapon from '../components/Weapon';

const GameScreen = ({ navigation }) => {
  const { gameState, loading, error, startNewGame, selectCard, avoidRoom } = useGame();

  useEffect(() => {
    startNewGame();
  }, []);

  useEffect(() => {
    if (error) {
      Alert.alert('Error', error);
    }
  }, [error]);

  if (loading && !gameState) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" />
        <Text>Loading game...</Text>
      </View>
    );
  }

  if (!gameState) return null;

  return (
    <ScrollView style={styles.container}>
      <HealthBar health={gameState.health} maxHealth={20} />
      
      <View style={styles.weaponContainer}>
        <Weapon weapon={gameState.equipped_weapon} monsters={gameState.slain_monsters} />
      </View>
      
      <View style={styles.roomContainer}>
        <Text style={styles.sectionTitle}>Current Room</Text>
        <Room 
          cards={gameState.current_room} 
          onSelectCard={selectCard}
          disabled={loading}
        />
      </View>
      
      <View style={styles.actionsContainer}>
        <Button 
          mode="contained" 
          onPress={avoidRoom}
          disabled={loading || gameState.avoided_previous_room}
          style={styles.button}
        >
          Avoid Room
        </Button>
        
        <Text style={styles.deckInfo}>
          Cards remaining in dungeon: {gameState.cards_remaining}
        </Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  roomContainer: {
    marginVertical: 16,
  },
  weaponContainer: {
    marginVertical: 16,
  },
  actionsContainer: {
    marginTop: 16,
    alignItems: 'center',
  },
  button: {
    marginVertical: 8,
    width: '80%',
  },
  deckInfo: {
    marginTop: 16,
    fontSize: 16,
  },
});

export default GameScreen;