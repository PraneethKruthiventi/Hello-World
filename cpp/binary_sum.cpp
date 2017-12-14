#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	cin >> T;
	while(T-- > 0)
	{
		string a, b;
		int x, y, i, pow=1, ans;
		cin >> a >> b;
		for(i = 0; i < a.size(); i++)
		{
			x += int(a[i])*pow;
			pow *= 2;
		}
		pow = 1;
		for(i = 0; i < a.size(); i++)
		{
			y += int(b[i])*pow;
			pow *= 2;
		}
		ans = x + y;
		string bin_ans;
		while(ans)
		{
			bin_ans += ans % 2;
			ans = ans/2; 
		}
		for(i = bin_ans.size()-1; i >= 0; i--)
			cout << bin_ans[i];
		cout << endl;
	}
	return 0;
}