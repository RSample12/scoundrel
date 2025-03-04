import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';

const Deck = ({ cardsRemaining }) => {
  // Generate a stack of cards visual, with thicker stack when more cards
  const stackLayers = Math.min(10, Math.ceil(cardsRemaining / 5));
  
  return (
    <View style={styles.container}>
      <View style={styles.deckContainer}>
        {[...Array(stackLayers)].map((_, index) => (
          <View 
            key={index} 
            style={[
              styles.deckCard, 
              { 
                top: index * 1, 
                left: index * 1,
                zIndex: 10 - index 
              }
            ]} 
          />
        ))}
        <View style={[styles.deckCard, styles.topCard]}>
          <Text style={styles.deckCount}>{cardsRemaining}</Text>
        </View>
      </View>
      <Text style={styles.label}>Dungeon</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    marginHorizontal: 10,
  },
  deckContainer: {
    width: 70,
    height: 100,
    marginBottom: 5,
  },
  deckCard: {
    position: 'absolute',
    width: 70,
    height: 100,
    backgroundColor: '#222',
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#555',
  },
  topCard: {
    backgroundColor: '#1e2a3d',
    justifyContent: 'center',
    alignItems: 'center',
    borderColor: '#444',
    zIndex: 11,
  },
  deckCount: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 20,
  },
  label: {
    color: '#666',
    fontSize: 12,
  }
});

export default Deck;