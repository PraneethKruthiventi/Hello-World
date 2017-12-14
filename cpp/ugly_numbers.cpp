#include <bits/stdc++.h>
using namespace std;
int ugly_number(int n)
{
	int ugly[n];
	ugly[0] = 1;
	int i2 = 0, i3 = 0, i5 = 0;
	int ugly_n, ugly_i2 = 2, ugly_i3 = 3, ugly_i5 = 5;
	for(int i=1; i<n; i++)
	{
		ugly_n = min(min(ugly_i2,ugly_i3), ugly_i5);
		ugly[i] = ugly_n;
		if(ugly_n == ugly_i2)
		{
			i2++;
			ugly_i2 = ugly[i2]*2;
		}
		if(ugly_n == ugly_i3)
		{
			i3++;
			ugly_i3 = ugly[i3]*3;
		}
		if(ugly_n == ugly_i5)
		{
			i5++;
			ugly_i5 = ugly[i5]*5;
		}
		cout << ugly_n << " ";
	}
	return ugly_n;
}
int main()
{
	int n;
	cin >> n;
	cout <<  endl << n << "th ugly number is " << ugly_number(n);
	return 0;
}