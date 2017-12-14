#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	cin >> T;
	while(T-- > 0)
	{
		int n, W, i, j;
		cin >> n >> W;
		int weight[n], value[n];
		for(i=0; i<n; i++)
			cin >> value[i];
		for(i=0; i<n; i++)
			cin >> weight[i];
			
		int K[n+1][W+1];
		for(i=0; i<=n; i++)
		{
		    for(j=0; j<=W; j++)
		    {
		        if(i==0 || j==0)
		            K[i][j] = 0;
		        else if(weight[i-1] > j)
		            K[i][j] = K[i-1][j];
		        else
		            K[i][j] = max(K[i-1][j], value[i-1] + K[i-1][j-weight[i-1]]);
		    }
		}
		cout << K[n][W] << endl;
	}
	return 0;
}