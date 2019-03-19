#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef vector<pii > vpii;

#define pb push_back

int main()
{
  int d[2], s[2];
  for (int i=0; i<2; i++){
    scanf("%d %d", d+i, s+i);
  }
  for (int i=0; i<2; i++){
    printf("%d %d\n", d[i], s[i]);
  }
return 0;
}
