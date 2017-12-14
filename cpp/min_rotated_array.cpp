#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	cin >> T;
	while(T-- > 0)
	{
		int n,i;
		cin >> n;
		int input[n];
		for(i=0; i<n; i++)
			cin >> input[i];
		int start = 0, end = n-1, mid;
		while(start <= end)
		{
			mid = (start + end)/2;
			if(mid == 0)
			{
				cout << min(input[0], input[1]) << endl;
				break;
			}
			if(input[mid] < input[mid-1])
			{
				cout << input[mid] << endl;
				break;
			}
			else if(input[end] < input[mid])
				start = mid+1;
			else
				end = mid-1;
		}
	}
	return 0;
}