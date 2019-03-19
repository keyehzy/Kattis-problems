#include <bits/stdc++.h>

using namespace std;

int W, n;

int readInt () {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}

int main(){
  W = readInt(), n = readInt();
  // scanf("%d\n%d", &W, &n);
    //cin >> W >> n;
  int a = 0, ww, ll;
  for (int i = 0; i < n; i++){
    ww = readInt(), ll = readInt();
    //    cin >> ww >> ll;
    a += ww*ll;   
  }
  cout << a / W;
}
