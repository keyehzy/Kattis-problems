#include <bits/stdc++.h>

using namespace std;

int m, n;

int main(){
  cin >> m >> n;
  int tot = 0;
  if (n % 2 == 0){
    tot += m * (n / 2);      
  } else{
    if (m % 2 == 0){
      tot += floor(n/2)*m + m / 2;
    } else{
      tot += floor(n/2)*m + floor(m/2);
    }    
  }
  cout << tot << endl;
}
