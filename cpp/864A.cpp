#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int n, i, temp1=0, temp2=0, count1=0, count2=0;
	cin >> n;
	long long int a[n];
	for(i=0; i<n; i++)
	{
		cin >> a[i];
		if(temp1 == 0)
			temp1 = a[i];
		else if(temp2 == 0 && temp1 != a[i])
			temp2 = a[i];
		else if(temp1 != a[i] && temp2 != a[i])
		{
			cout << "NO";
			return 0;
		}
		else
		{
			if(a[i] == temp1)
				count1++;
			else if (a[i] == temp2)
				count2++;
		}
	}
	if(temp1 == 0 || temp2 == 0 || count1 != count2)
		cout << "NO";
	else
		cout << "YES" << endl << temp2 << " " << temp1;
	return 0;
}