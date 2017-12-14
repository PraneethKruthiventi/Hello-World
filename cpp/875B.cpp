#include <iostream>
using namespace std;

int main()
{
	long long int n;
	cin >> n;
	long long int a[n];
	long long int i;
	long long int sol[n+1];
	long long int updated_array[n] = {0};
	for(i = 1; i < n+1; i++)
		cin >> a[i];

	sol[0] = 1;
	sol[n] = 1;
	long long int end_index = n-1;
	long long int count = 0;
	cout << sol[0];
	for(i = 1; i < n; i++)	
	{
		updated_array[a[i]] = 1;
		count += 1;
		if(a[i] == end_index)
			end_index--;
		sol[i] = count + end_index - n + 1;
		cout << sol[i] << " "; 
	}
	cout << sol[n];
	cout << endl;
	return 0;
}
