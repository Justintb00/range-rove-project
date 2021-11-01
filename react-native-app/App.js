import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Image, ImageBackground } from 'react-native';
import {WebView} from 'react-native-webview';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Welcome to React Native!</Text>
      <Text>We will insert a checker for seeing if a camera is available here.</Text>
      <Image>
        source= {{uri: "http://localhost:3005/video"}},
        style={styles.image}
      </Image>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    width: 300,
    height: 300
  }
});
