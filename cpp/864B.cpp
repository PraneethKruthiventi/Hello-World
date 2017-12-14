#include <bits/stdc++.h>
using namespace std;
int check(string input, int start, int end)
{
	int array[26] = {0};
	int count=0;
	//cout << start+1 << " " << end-1 << endl;
	for(int i = start+1; i < end; i++)
	{
		if(isupper(input[i]))
		{
			//cout  << input[i] << endl;
			return 0;
		}
		else
		{
			array[input[i]-'a'] += 1;
			if(array[input[i]-'a'] == 1)
				count++;
		}
	}
	//cout << "count " << count << endl;
	return count;
}
int main()
{
	int n, i;
	string input;
	cin >> n;
	cin >> input;
	int start = 0, ans = check(input, -1, n);
	
	for(i=0;i<n;i++)
	{
		if(isupper(input[i]))
		{
			if(i == 0)
				ans = max(check(input, -1, i), ans);
			else
				ans = max(check(input, start, i), ans);
			//cout << "**" << endl;
			start = i;
		}
		else if(i == n-1)
		{	
			ans = max(check(input, start, n), ans);
		}
	}
	cout << ans;
	return 0;
}