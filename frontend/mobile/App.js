import React, { useState } from "react";
import { View, TextInput, Button, Text } from "react-native";
import axios from "axios";

export default function App() {
  const [domain, setDomain] = useState("");
  const [output, setOutput] = useState("");

  const createCourse = async () => {
    const res = await axios.post("http://YOUR_SERVER/create_course", null, {
      params: { domain }
    });
    setOutput(JSON.stringify(res.data));
  };

  return (
    <View>
      <TextInput placeholder="Domain" onChangeText={setDomain} />
      <Button title="Create Course" onPress={createCourse} />
      <Text>{output}</Text>
    </View>
  );
}
