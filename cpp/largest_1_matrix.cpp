#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i, j;
	cin >> n;
	int a[n][n], dp[n][n];
	int max = 0, max_i, max_j;
	for(i=0; i<n; i++)
		for(j=0; j<n; j++)
		{
			cin >> a[i][j];
			if(i==0 || j==0)
			{
				dp[i][j] = a[i][j];
				if(dp[i][j] > max)
				{
					max = dp[i][j];
					max_i = i;
					max_j = j;
				}
			}
		}
	for(i=1; i<n; i++)
	{
		for(j=1; j<n; j++)
		{
			if(a[i][j] == 1)
			{
				dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
				if(dp[i][j] > max)
				{
					max = dp[i][j];
					max_i = i-max+1;
					max_j = j-max+1;
				}
			}
			else
			{
				dp[i][j] == 0;
			}
		}
	}
	cout << "i=" << max_i << " j="<< max_j << " size = "<< max << endl;
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
			cout << dp[i][j] << " ";
		cout << endl;
	}
	return 0;
}