//k buys and sells.
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i, k;
	cin >> n >> k;
	int a[n];
	int min, max;
	int ans[n] = {0}, x=0;
	for(i=0;i<n;i++)
		cin >> a[i];
	i = 0;
	while(i < n-1)
	{
		while(i<n-1 && a[i+1] <= a[i])
			i++;
		min = a[i++];
		while(i<n && a[i] >= a[i-1])
			i++;
		max = a[i-1];
		ans[x] = max-min;
		x++;
	}	
	sort(ans, ans+x);
	int answer = 0;
	x--;
	while(k-- > 0)
		answer += ans[x--];
	cout << answer;
	return 0;
}


/*
//if only one buy and sell is allowed
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i;
	cin >> n;
	int a[n];
	int smallest = 9999, ans=0;
	for(i=0; i<n; i++)
	{
		cin >> a[i];
		if(a[i] < smallest)
			smallest = a[i];
		ans = max(ans, a[i]-smallest);
	}
	cout << ans;
}
*/