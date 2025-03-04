import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Provider as PaperProvider } from 'react-native-paper';
import { GameProvider } from './contexts/GameContext';

import HomeScreen from './screens/HomeScreen';
import GameScreen from './screens/GameScreen';
import RulesScreen from './screens/RulesScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <PaperProvider>
      <GameProvider>
        <NavigationContainer>
          <Stack.Navigator initialRouteName="Home">
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Game" component={GameScreen} />
            <Stack.Screen name="Rules" component={RulesScreen} />
          </Stack.Navigator>
        </NavigationContainer>
      </GameProvider>
    </PaperProvider>
  );
}
