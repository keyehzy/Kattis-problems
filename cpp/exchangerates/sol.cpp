#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back
int n;

int main(){
  while (1){
    cin >> n;
    if (n == 0) break;
    if (n < 2) {
      printf("%.2lf\n", 1000.00);
      break;
    }
    double a[n], mxc = 100000.0, mxu = 0.0;
    for (int i = 0; i < n; i++) scanf("%lf", a+i);

    for (auto& r: a){
      mxc = max(mxc, round(mxu*r*0.97));
      mxu = max(mxu, round(mxc*0.97/r));
      // cout << r << " " << mxc << " " << mxu << endl;
    }
    printf("%.2lf\n", mxc/100.0);
  }
}
