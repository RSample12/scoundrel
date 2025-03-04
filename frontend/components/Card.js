import React from 'react';
import { TouchableOpacity, View, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';

const getSuitColor = (suit) => {
  if (suit === 'hearts' || suit === 'diamonds') {
    return '#e53935'; // Red
  }
  return '#212121'; // Black
};

const getSuitSymbol = (suit) => {
  switch (suit) {
    case 'hearts': return '♥';
    case 'diamonds': return '♦';
    case 'clubs': return '♣';
    case 'spades': return '♠';
    default: return '';
  }
};

const getCardValue = (value) => {
  switch (value) {
    case 1: return 'A';
    case 11: return 'J';
    case 12: return 'Q';
    case 13: return 'K';
    case 14: return 'A';
    default: return value.toString();
  }
};

const getCardTypeInfo = (type) => {
  switch (type) {
    case 'monster':
      return { label: 'Monster', color: '#f8f8f8', borderColor: '#9e9e9e' };
    case 'weapon':
      return { label: 'Weapon', color: '#e0f7fa', borderColor: '#4fc3f7' };
    case 'potion':
      return { label: 'Potion', color: '#f1f8e9', borderColor: '#8bc34a' };
    default:
      return { label: '', color: '#fff', borderColor: '#ddd' };
  }
};

const Card = ({ card, onPress, disabled }) => {
  if (!card) return <View style={[styles.card, styles.emptyCard]} />;

  const { suit, value, type } = card;
  const color = getSuitColor(suit);
  const symbol = getSuitSymbol(suit);
  const displayValue = getCardValue(value);
  const typeInfo = getCardTypeInfo(type);
  
  return (
    <TouchableOpacity 
      style={[
        styles.card, 
        { backgroundColor: typeInfo.color, borderColor: typeInfo.borderColor }
      ]} 
      onPress={() => onPress && onPress(card)}
      disabled={disabled}
      activeOpacity={0.7}
    >
      <View style={styles.cornerTop}>
        <Text style={[styles.value, { color }]}>{displayValue}</Text>
        <Text style={[styles.suit, { color }]}>{symbol}</Text>
      </View>
      
      <Text style={[styles.centerSuit, { color }]}>{symbol}</Text>
      
      <View style={styles.typeLabel}>
        <Text style={styles.typeLabelText}>{typeInfo.label}</Text>
      </View>
      
      <View style={[styles.cornerBottom]}>
        <Text style={[styles.value, { color }]}>{displayValue}</Text>
        <Text style={[styles.suit, { color }]}>{symbol}</Text>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  card: {
    width: 80,
    height: 120,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: '#ddd',
    backgroundColor: 'white',
    padding: 8,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
    margin: 5,
  },
  emptyCard: {
    borderStyle: 'dashed',
    borderColor: '#aaa',
    backgroundColor: '#f5f5f5',
  },
  cornerTop: {
    position: 'absolute',
    top: 8,
    left: 8,
    alignItems: 'center',
  },
  cornerBottom: {
    position: 'absolute',
    bottom: 8,
    right: 8,
    alignItems: 'center',
    transform: [{ rotate: '180deg' }],
  },
  value: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  suit: {
    fontSize: 16,
  },
  centerSuit: {
    fontSize: 36,
  },
  typeLabel: {
    position: 'absolute',
    bottom: 8,
    left: 8,
    backgroundColor: 'rgba(255,255,255,0.7)',
    paddingHorizontal: 3,
    borderRadius: 2,
  },
  typeLabelText: {
    fontSize: 8,
    fontWeight: 'bold',
  }
});

export default Card;