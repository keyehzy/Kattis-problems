#include <bits/stdc++.h>

using namespace std;

char t;
string s;

void encode(string s){
  for (unsigned i = 0; i < s.size(); i++){
    int count = 1;
    for (unsigned j = i+1; j < s.size(); j++) {
      if (s[i] == s[j]) {
	count++;
      } else {
	break;
      }
    }
    i += count-1;
    cout << s[i] << count; 
  }
  return;
}

void decode(string s){
  for (unsigned i = 0; i < s.size()-1;){
    for (int j = 1; j <= s[i+1]-'0'; j++){
      cout << s[i];
    }
    i += 2;
  }
  return;
}

int main(){
  cin >> t >> s;

  if (t == 'E') {
    encode(s);
  } else if (t == 'D'){
    decode(s);
  }
}
