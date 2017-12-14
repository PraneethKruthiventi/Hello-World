#include <iostream>
using namespace std;

int main()
{
	long long int T;
	cin >> T;
	while(T-- > 0)
	{
		long long int n;
		long long int i;
		cin >> n;
		long long int a[n];
		long long int largest_so_far[n]={0};
		for(i = 0; i < n; i++)
		{
			cin >> a[i];
			if(i > 0)
				largest_so_far[i] = max(largest_so_far[i-1], a[i]);
			else
				largest_so_far[i] = a[i];
		}
		for(i = 0; i < n; i++)
		{
			
		}
	}
	return 0;
}	