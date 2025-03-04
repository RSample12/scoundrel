import React from 'react';
import { ScrollView, View, StyleSheet } from 'react-native';
import { Text, Button } from 'react-native-paper';

const RuleSection = ({ title, children }) => (
  <View style={styles.section}>
    <Text style={styles.sectionTitle}>{title}</Text>
    {children}
  </View>
);

const RulesScreen = ({ navigation }) => {
  return (
    <ScrollView style={styles.container}>
      <RuleSection title="Overview">
        <Text style={styles.text}>
          Scoundrel is a single-player card game where you delve into a dungeon,
          fighting monsters with weapons and using potions to survive.
        </Text>
      </RuleSection>

      <RuleSection title="Card Types">
        <Text style={styles.text}>• Monsters (Clubs & Spades)</Text>
        <Text style={styles.subtext}>
          - Must be fought with a weapon or barehanded{'\n'}
          - Their value is their damage{'\n'}
          - Face cards and Aces have special values
        </Text>
        
        <Text style={styles.text}>• Weapons (Diamonds)</Text>
        <Text style={styles.subtext}>
          - Used to fight monsters{'\n'}
          - Can only fight monsters of equal or lesser value than the last monster killed{'\n'}
          - Picking up a new weapon discards the old one and its monster stack
        </Text>
        
        <Text style={styles.text}>• Potions (Hearts)</Text>
        <Text style={styles.subtext}>
          - Heal for their face value{'\n'}
          - Only one potion can be used per room{'\n'}
          - Maximum health is 20
        </Text>
      </RuleSection>

      <RuleSection title="Gameplay">
        <Text style={styles.text}>1. Each turn, you enter a room with up to 4 cards</Text>
        <Text style={styles.text}>2. You must choose 3 cards from the room in any order</Text>
        <Text style={styles.text}>3. You can avoid a room (skip it) but not twice in a row</Text>
        <Text style={styles.text}>4. The game ends when:</Text>
        <Text style={styles.subtext}>
          - You die (health reaches 0){'\n'}
          - You complete the dungeon (use all cards)
        </Text>
      </RuleSection>

      <RuleSection title="Combat">
        <Text style={styles.text}>Without a weapon:</Text>
        <Text style={styles.subtext}>
          - Take full monster damage{'\n'}
          - Monster is discarded
        </Text>
        
        <Text style={styles.text}>With a weapon:</Text>
        <Text style={styles.subtext}>
          - Take damage = monster value - weapon value{'\n'}
          - Monster is added to weapon's stack{'\n'}
          - Can only fight monsters ≤ last killed monster
        </Text>
      </RuleSection>

      <RuleSection title="Scoring">
        <Text style={styles.text}>If you die:</Text>
        <Text style={styles.subtext}>
          Score = -(abs(health) + remaining monster values)
        </Text>
        
        <Text style={styles.text}>If you complete the dungeon:</Text>
        <Text style={styles.subtext}>
          Score = remaining health{'\n'}
          Bonus: If last card was a potion and health is 20,{'\n'}
          add potion value to score
        </Text>
      </RuleSection>

      <View style={styles.buttonContainer}>
        <Button
          mode="contained"
          onPress={() => navigation.navigate('Game')}
          style={styles.button}
        >
          Start Playing
        </Button>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#2C3E50',  // Dark blue background
    padding: 16,
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ECF0F1',  // White text
    marginBottom: 12,
  },
  text: {
    fontSize: 16,
    color: '#ECF0F1',  // White text
    marginBottom: 8,
  },
  subtext: {
    fontSize: 14,
    color: '#BDC3C7',  // Light gray text
    marginLeft: 16,
    marginBottom: 16,
  },
  buttonContainer: {
    marginVertical: 24,
    alignItems: 'center',
  },
  button: {
    width: '80%',
  },
});

export default RulesScreen;
