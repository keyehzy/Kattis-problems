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
    int s;
    scanf("%d", &s);
    int top = (s>>1) + ((s&1) ? 2 : 1);
    printf("%d:\n", s);
    for (int i = 2; i < top; i++)
    {
        int rem = s % ((i << 1) - 1);
        if (rem == 0 || rem == i) printf("%d,%d\n", i, i - 1);
        if (s % i == 0) printf("%d,%d\n", i, i);
    }
    return 0;
}
