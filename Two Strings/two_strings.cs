// Complete the twoStrings function below.
static string twoStrings(string s1, string s2) {
  char[] characters = "abcdefghijklmnopqrstuvwxyz1234567890".ToCharArray();
  foreach(char c in characters) {
    if (s1.Contains(c) && s2.Contains(c)) {
      return "YES";
    }
  }
  return "NO";
}
﻿