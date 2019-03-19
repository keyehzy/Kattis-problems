#include <bits/stdc++.h>

using namespace std;

int n;          // grid lenght
int a[105][105];  // initializing with max length

int main(){
  while(cin >> n){
    if (n==-1) break; // breaking out of the loop
    for (int i = 0; i < n; i++){  // initalizing array
      for (int j = 0; j < n; j++){
	cin >> a[i][j];
      }
    }
    // here we are going to use the following properties of adjency matrices
    // first is that the square of it is the number of 2-length paths
    // that is, the vertices of the a2 means that we can reach this point
    // walking two steps of the graph
    // the cube is the same for the 3-length path
    // by definition the vertice does not form a triangule if it can not
    // be reached by 3 steps in the graph
    
    // O(n^3) matrix multiplication (ok until n ~ 10000 for 1s assuming
    // typical computer is a dozen of MIPS)
    int a2[105][105];
    for (int i = 0; i < n; i++){
      for (int j  = 0; j  < n; j ++){
	int sum = 0;
	for (int k = 0; k < n; k++){
	  sum += a[i][k] * a[k][j];
	}
	a2[i][j] = sum;
      }
    }
    int a3[105][105];
    for (int i = 0; i < n; i++){
      for (int j  = 0; j  < n; j ++){
	int sum = 0;
	for (int k = 0; k < n; k++){
	  sum += a2[i][k] * a[k][j];
	}
	a3[i][j] = sum;
      }
    }
    
    for (int i = 0; i < n; i++){
      if(a3[i][i] == 0){
	printf("%d ", i);
      }
    }
    cout << '\n';
  }
}
