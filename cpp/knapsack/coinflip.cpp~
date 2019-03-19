#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back

vi denom;
int n = 10;
int dp[1000];

int f(int n){
  if (dp[n] != -1) {
    return dp[n];
  }
  if (n <= 0) {
    return 0;
  }
  int ans = 1 << 20;
  for (auto& it: denom){
    if (n-it >= 0){
      ans = min(ans, 1+f(n-it));
    }
  }
  dp[n] = ans;
  return ans;
}

int main(){
  fill_n(dp, sizeof(dp)/sizeof(dp[0]), -1);
  denom.pb(1);
  denom.pb(3);
  denom.pb(4);
  printf("%d\n", f(n));
}
