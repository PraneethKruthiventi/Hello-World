#include <bits/stdc++.h>
using namespace std;
struct Loc {
	long long int x, minimum;
};
Loc findMin(long long int array[], long long int size)
{
	Loc temp;
	temp.minimum = array[size];
	temp.x = size;
	for(int i = 1; i < size; i++)
		if(array[size] < temp.minimum)
		{
			temp.minimum = array[size];
			temp.x = size;
		}
	return temp;
}
int main()
{
	long long int T;
	cin >> T;
	while(T-- > 0)
	{
		long long int n,k;
		cin >> n >> k;
		long long int i,j;
		long long int a[n][n];
		long long int row_array[n]={0}, col_array[n]={0};
		Loc row, col;
		long long int ans = 0;
		for(i=0;i<n;i++)
			for(j=0;j<n;k++)
			{
				cin >> a[i][j];
				row_array[i] += a[i][j];
				col_array[j] += a[i][j];
			}
		row = findMin(row_array, n);
		col = findMin(col_array, n);
		for(i=0;i<k;i++)
		{
			if(col.minimum < row.minimum)
			{
				ans += col.minimum;
				col_array[col.x] += n;
				for(int i = 0; i < n; i++)
					row_array[i] += 1;
				row = findMin(row_array, n);
				col = findMin(col_array, n);
			}
			else
			{
				ans += row.minimum;
				row_array[row.x] += n;
				for(int i = 0; i < n; i++)
					col_array[i] += 1;
				row = findMin(row_array, n);
				col = findMin(col_array, n);
			}
		}
		cout << ans << endl;
	}
	return 0;
}

