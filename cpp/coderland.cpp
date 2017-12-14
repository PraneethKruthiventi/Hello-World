#include <iostream>
using namespace std;

int main()
{
	long long int T;
	cin >> T;
	while(T--)
	{
		int n;
		cin >> n;
		int cost[n];	
		int req[n];
		for(int i = 0; i < n; i++)
			cin >> cost[i];
		for(int i = 0; i < n; i++)
			cin >> req[i];
		int sol = cost[0]*req[0];
		int curr_cost = cost[0];
		for(int i = 1; i < n; i++ )
		{ 
			curr_cost = min(curr_cost, c[i]);
			sol+= curr_cost*req[i];
		} 
		cout << sol << endl;
	}
	return 0;
}