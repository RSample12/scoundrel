import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Text } from 'react-native-paper';
import Card from './Card';

const Weapon = ({ weapon, monsters = [] }) => {
  if (!weapon) {
    return (
      <View style={styles.container}>
        <Text style={styles.noWeaponText}>No weapon equipped</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Equipped Weapon</Text>
      <ScrollView horizontal showsHorizontalScrollIndicator={false}>
        <View style={styles.weaponContainer}>
          <Card card={weapon} />
          
          {/* Display stacked monsters slain by this weapon */}
          <View style={styles.monstersContainer}>
            {monsters.map((monster, index) => (
              <View 
                key={index} 
                style={[
                  styles.slainMonster,
                  { left: 30 + (index * 20) }
                ]}
              >
                <Card card={monster} />
              </View>
            ))}
          </View>
        </View>
      </ScrollView>
      
      {/* Display weapon power vs the last monster */}
      {weapon && monsters.length > 0 && (
        <View style={styles.statsContainer}>
          <Text style={styles.statsText}>
            Weapon Power: {weapon.value} vs Last Monster: {monsters[monsters.length - 1].value}
          </Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 8,
    marginLeft: 10,
  },
  weaponContainer: {
    flexDirection: 'row',
    marginLeft: 10,
    height: 130,
  },
  monstersContainer: {
    position: 'relative',
    marginLeft: -20,
    flexDirection: 'row',
  },
  slainMonster: {
    position: 'absolute',
    top: 0,
  },
  noWeaponText: {
    textAlign: 'center',
    color: '#777',
    fontStyle: 'italic',
    padding: 10,
  },
  statsContainer: {
    marginTop: 5,
    alignItems: 'center',
  },
  statsText: {
    fontSize: 12,
    color: '#555',
  }
});

export default Weapon;