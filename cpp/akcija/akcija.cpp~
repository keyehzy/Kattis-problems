#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back


int main(){
  int n;
  scanf("%d", &n);
  int a[n];
  for (int i = 0; i < n; ++i){
    scanf("%d", &a[i]);
  }

  int m = 100000;
  int idx = 0;
  for (int i = 0; i < n; ++i){
    if (a[i] < m) {
      m = a[i];
      idx = i;
    }
  }
  printf("%d\n", idx);
}

