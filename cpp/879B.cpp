#include <iostream>
using namespace std;

int main()
{
	long long int n;
	long long int k;
	cin >> n >> k;
	long long int p[n];
	long long int max_so_far[n];
	long long int max_how_long[n];
	for(long long int i = 0; i < n; i++)
	{
		cin >> p[i];
		if(i==0)
		{
			max_so_far[i] = p[i];
			max_how_long[i] = 1;
		}
		else
		{
			max_so_far[i] = max(p[i], max_so_far[i-1]);
			if(max_so_far[i] == max_so_far[i-1])
			{	
				max_how_long[i] = max_how_long[i-1] + 1;
				if(max_how_long[i] == k+1)
				{
					cout << max_so_far[i] << endl;
					return 0;
				}
			}
			else
			{
				max_how_long[i] = 2;

			}
		}	
	}
	if(n==2)
		cout << max(p[0], p[1]);
	else
	{
		cout << max_so_far[n-1] << endl;
	}

	return 0;
}
