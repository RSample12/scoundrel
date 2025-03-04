import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';

const HealthBar = ({ health, maxHealth = 20 }) => {
  const percentage = Math.max(0, Math.min(100, (health / maxHealth) * 100));
  
  // Determine color based on health percentage
  let barColor = '#4caf50'; // Green
  if (percentage < 30) {
    barColor = '#f44336'; // Red
  } else if (percentage < 60) {
    barColor = '#ff9800'; // Orange
  }
  
  return (
    <View style={styles.container}>
      <View style={styles.barContainer}>
        <View style={[styles.bar, { width: `${percentage}%`, backgroundColor: barColor }]} />
      </View>
      <Text style={styles.text}>{health} / {maxHealth} HP</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
  },
  barContainer: {
    height: 16,
    width: '100%',
    backgroundColor: '#e0e0e0',
    borderRadius: 8,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: '#bdbdbd',
  },
  bar: {
    height: '100%',
  },
  text: {
    marginTop: 4,
    textAlign: 'center',
    fontWeight: 'bold',
  }
});

export default HealthBar;