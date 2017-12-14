#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i;
	cin >> n;
	int a[n], sumleft[n+1]={0};
	int first = -1, last = 0;
	for(i=0; i<n; i++)
	{
		cin >> a[i];
		if(a[i] == 0)
			a[i] = -1;
		sumleft[i+1] = sumleft[i] + a[i];
		if(first == -1 && sumleft[i+1] == 0)
			first = i;
		if(sumleft[i+1] == 0)
			last = i;
	}
	cout << first << " " << last << endl;
	return 0;
}