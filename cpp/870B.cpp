#include <iostream>
using namespace std;

int main()
{
	long long int n,k;
	cin >> n >> k;
	long long int a[n];
	long long int maxi = -999999999999; 
	long long int min = 999999999999;
	for (long long int i = 0; i < n; i++)
	{
		cin>>a[i];
		if(a[i] > maxi)
			maxi = a[i];
		if(a[i] < min)
			min = a[i];
	}
	if(k==1)
		cout << min << endl;
	else if(k==2)
		cout << max(a[0],a[n-1]);
	else if (k!=2)
		cout << maxi << endl;
	return 0;
}