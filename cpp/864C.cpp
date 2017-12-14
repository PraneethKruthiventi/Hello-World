#include <bits/stdc++.h>
using namespace std;

int main()
{
	long long int a, b, f, k, i;
	cin >> a >> b >> f >> k;
	long long int pos = 0, fuel = b, ans = 0;
	if (a - f > b)
	{
		cout << "-1";
		return 0;
	}
	for(i = 0; i < k; i++)
	{
		//cout << i << " " << pos << " " << fuel << " " << ans << endl; 
		if(pos == 0)
		{
			if(fuel < a || (fuel < 2*a-f && i != k-1))
			{
				ans++;
				fuel = b+f;
				pos = a;
			}
			else
			{
				pos = a;
			}
		}
		else
		{
			if(fuel < a || (fuel < a+f && i != k-1))
			{
				ans++;
				fuel = b-f+a;
				pos = 0;
			}
			else
			{
				pos = 0;
			}
		}
		fuel -= a;
		//cout << i << " " << pos << " " << fuel << " " << ans << endl; 	
	}
	cout << ans;
	return 0;
}