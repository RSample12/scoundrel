import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Text } from 'react-native-paper';
import Card from './Card';

const Room = ({ cards = [], onSelectCard, disabled }) => {
  // Handle selecting a card - convert index to the actual card object
  const handleCardPress = (cardIndex) => {
    if (onSelectCard) {
      onSelectCard(cardIndex);
    }
  };
  
  return (
    <View style={styles.container}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.roomContainer}>
        {cards.map((card, index) => (
          <Card
            key={index}
            card={card}
            onPress={() => handleCardPress(index)}
            disabled={disabled}
          />
        ))}
        
        {/* Add empty card placeholders if we have fewer than 4 cards */}
        {[...Array(Math.max(0, 4 - cards.length))].map((_, index) => (
          <View key={`empty-${index}`} style={styles.emptySlot} />
        ))}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
  },
  roomContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 10,
  },
  emptySlot: {
    width: 80,
    height: 120,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ddd',
    borderStyle: 'dashed',
    backgroundColor: '#f5f5f5',
    margin: 5,
  },
});

export default Room;