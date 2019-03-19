#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back


int main(){
  int n; cin >> n;
  vi tot;
  for (int i = 0; i < n; ++i){
    int ii; cin >> ii;
    tot.push_back(ii);
  }
  sort(tot.rbegin(), tot.rend());

  int s = 0, j = 0;
  while (j < (int)tot.size() - 2){
    s += tot[j] + tot[j+1];
    j += 3;
      }
  while (j < (int)tot.size()){
      s += tot[j];
      j += 1;
    }
  printf("%d\n", s);

}
