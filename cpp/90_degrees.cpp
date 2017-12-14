#include <bits/stdc++.h>
using namespace std;
int main()
{
	int m, n, i, j;
	cin >> m >> n;
	char input[m][n], input_90[n][m];
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		{
			cin >> input[i][j];
			input_90[j][i] = input[i][j];
		}
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)	
			cout << input_90[i][j] << " ";
		cout << endl;
	}
	
	return 0;
}