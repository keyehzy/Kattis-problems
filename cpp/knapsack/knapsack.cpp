#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back

int n = 5;
int vals[] = {1, 2, 3, 4, 5};
int wt[] = {1, 1, 1, 2, 2};
int dp[1000][1000];
int f(int idx, int wleft){
  cout << idx << endl;
  if (idx >= n){
    return 0;
  }
  if (dp[idx][wleft] != -1){
    return dp[idx][wleft];
  }
  int ans = 0;
  if (wt[idx] <= wleft){
    ans = max(f(idx+1, wleft), vals[idx] + f(idx+1, wleft-wt[idx]));
  }
  dp[idx][wleft] = ans;
  return ans;
}
  // for each item[idx] we can either take it or ignore it
  // if we take it check if we have enough space
  // f(idx, wleft) = max(f(idx + 1, wleft), vals[idx] + f(idx+1, wleft - wt[idx]))

int main(){
  for (int i = 0; i < 1000; i++){
    fill_n(dp[i], 1000, -1);
  }
  cout << f(0, 5) << endl;
  // maximum weight = W
  // num of valuable = N
}
