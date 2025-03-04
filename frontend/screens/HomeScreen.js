import React, { useEffect } from 'react';
import { View, StyleSheet, Image } from 'react-native';
import { Text, Button } from 'react-native-paper';
import { useGame } from '../contexts/GameContext';
import { Alert } from 'react-native';
import * as ScreenOrientation from 'expo-screen-orientation';

const HomeScreen = ({ navigation }) => {
  const { gameState, startNewGame } = useGame();

  const handlePlayGame = async () => {
    await startNewGame();
    navigation.navigate('Game');
  };

  useEffect(() => {
    if (gameState) {
      Alert.alert(
        'Resume Game',
        'Would you like to resume your previous game?',
        [
          {
            text: 'New Game',
            onPress: handlePlayGame,
          },
          {
            text: 'Resume',
            onPress: () => navigation.navigate('Game'),
          },
        ]
      );
    }
  }, []);

  useEffect(() => {
    ScreenOrientation.lockAsync(ScreenOrientation.OrientationLock.PORTRAIT);
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Scoundrel</Text>
        <Text style={styles.subtitle}>A Roguelike Card Game</Text>
        
        {/* Add logo/image here if you have one */}
        {/* <Image source={require('../assets/logo.png')} style={styles.logo} /> */}
        
        <View style={styles.buttonContainer}>
          <Button
            mode="contained"
            onPress={handlePlayGame}
            style={styles.button}
          >
            Play Game
          </Button>
          
          <Button
            mode="outlined"
            onPress={() => navigation.navigate('Rules')}
            style={styles.button}
          >
            How to Play
          </Button>
        </View>
      </View>
      
      <Text style={styles.version}>Version 1.0.0</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#2C3E50',  // Dark blue background
    padding: 16,
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#ECF0F1',  // White text
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 18,
    color: '#ECF0F1',  // White text
    marginBottom: 32,
  },
  logo: {
    width: 200,
    height: 200,
    marginBottom: 32,
  },
  buttonContainer: {
    width: '100%',
    maxWidth: 300,
  },
  button: {
    marginVertical: 8,
  },
  version: {
    color: '#95A5A6',  // Gray text
    textAlign: 'center',
    marginBottom: 16,
  },
});

export default HomeScreen;
