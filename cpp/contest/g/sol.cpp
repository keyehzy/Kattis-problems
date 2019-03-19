#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

int x, y, n;
string instrs[] = {"Forward", "Right", "Left"};

pii walk(int dir, pii pos){

  for (int j = 0; j < n; j++){
    if (ins[j] == "Forward"){
      pos = walk(dir, pos);
    } else if (ins[j] == "Right"){
      dir = (dir+1) % 4;
    } else if (ins[j] == "Left"){
      dir = (dir-1) % 4;
    }
  
  if (dir == 0) pos.first++;
  else if (dir == 1) pos.second++;
  else if (dir == 2) pos.first--;
  else if (dir == 3) pos.second--;
  return pos;
}

int main(){
  cin >> x >> y >> n;
  string ins[n];
  for (int i = 0; i < n; i++) cin >> ins[i];


  bool found = false;

  for (int i = 0; i < n && !found; i++){
    string original = ins[i];
    int dir = 0;
    pii pos = make_pair(0,0);
    for (int k = 0; k < 3; k++){
      if(instrs[k] != original){
	ins[i] = instrs[k];

	  cout << pos.first << " " << pos.second << " " << j << endl;
	}
	if (pos.first == x && pos.second == y){
	  cout << i-1 << " " << instrs[k+1];
	  found = true;
	  break;
	} else {
	  ins[i] = original;
	}
      }
    }
  }
}
