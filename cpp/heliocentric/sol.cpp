#include <bits/stdc++.h>

using namespace std;

int e, m;

int main(){
  int c = 0;
  while(cin >> e >> m){
    int days = 0;
    c++;
    if (e==0 && m==0){
      printf("Case %d: %d", c, 0);
      continue;
    }
    while(e || m){
      e = (e % 365);
      m = (m % 687);
      days++;
    }
    cout << days << '\n';
  }

}
