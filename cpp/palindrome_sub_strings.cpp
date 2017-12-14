#include <bits/stdc++.h>
using namespace std;
set<string> unique_str;
void printUnique()
{
	set <string> :: iterator itr;
	cout << "unique palindromes = " << unique_str.size() << endl;
	for(itr = unique_str.begin(); itr != unique_str.end(); itr++)
		cout << *itr << endl;
}

void printStr(string input, int i, int j, int max_len)
{
	cout << "size " << max_len << " start " << i << " end " << j << " ";
	string temp = "";
	for(int x = i; x <= j; x++)
	{
		cout << input[x];
		temp += input[x];
	}
	unique_str.insert(temp);
	cout << endl;
}
int main()
{
	int n, i, j, k, count = 0;
	//cin >> n;
	/*char input[n];
	for(i=0; i<n; i++)
		cin >> input[i];*/
	string input;
	cin >> input;
	n = input.size();

	cout << "Input: ";
	for(i=0; i<n; i++)
		cout << input[i] << " ";
	cout << endl;

	int max_i, max_j, max_len = 1;
	int dp[n][n];
	//len 1
	for(i=0; i<n; i++)
	{
		dp[i][i] = 1;
		max_len = 1;
		printStr(input, i, i, max_len);
		count++;
	}
	//len 2
	for(i=0; i<n-1; i++)
	{
		j = i + 1;
		if(input[i] == input[j])
		{
			dp[i][j] = 1;
			max_len = 2; max_i = i; max_j = j;
			printStr(input, i, j, max_len);
			count++;
		}
		else
			dp[i][j] = 0;
	}
	//len 3 - n;
	for(k=3; k<=n; k++)
	{
		for(i=0; i<n-k+1; i++)
		{
			j = i + k - 1;
			if(input[i] == input[j] && dp[i+1][j-1])
			{
				dp[i][j] = 1;
				max_len = k; max_i = i; max_j = j;
				printStr(input, i, j, max_len);
				count++;
			}
			else
				dp[i][j] = 0;
		}
	}
	cout << "count " << count; 
	cout << endl <<"************"<<endl;
	printUnique();
	return 0;
}