#include <bits/stdc++.h>

using namespace std;

int a[105][105]; // decided to initialize this here with maximum size array
                 // this way we can access it with our function
int m, n, idx;

void floorfill (int x, int y){
  if (a[x][y] == 0 && x >= 0 && x < m && y>=0 && y < n){
    //cout << x << " " << y << '\n';
    a[x][y] = 1;
    floorfill(x+1, y);
    floorfill(x, y+1);
    floorfill(x-1, y);
    floorfill(x, y-1);
  }
}

int main(){
  idx = 1;
  while(cin >> m >> n){
    for (int i = 0; i < m; i++){   // iterating over the input
      for (int j = 0; j < n; j++){
	char d; cin >> d;           // two colors black (0) and white(1)
	if (d == '#') a[i][j] = 1;   // 1 if #
	if (d == '-') a[i][j] = 0;   // 0 if -	    
      }
    }
    // we'll try a simple recursive implementation of the floor fill algo
    // https://en.wikipedia.org/wiki/Flood_fill
    // O(m * n)
    int count = 0;
    for (int i = 0; i < m; i++){
      for (int j = 0; j < n; j++){
    	if (a[i][j] == 0){
    	  floorfill(i, j);
    	  count++;
    	}
      }
    }
    printf("Case %d: %d\n", idx, count);
    idx++;
  }
}
