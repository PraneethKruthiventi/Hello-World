#include <iostream>
using namespace std;

int main()
{
	long long int n;
	cin >> n;
	long long int a[n];
	long long int i;
	long long int sol[n+1];
	long long int updated_array[n] = {0}
	for(i = 1; i < n+1; i++)
		cin >> a[i];

	sol[0] = 1;
	sol[n] = 1;
	long long int end_index = n-1;
	long long int coubt = 0;
	for(i = 1; i < n; i++)	
	{
		updated_array[a[i]] = 1;
		count += 1;
		sol[i] = count - get_index(end_index);
	}
	for(i = 0; i < n+1; i++)
		cout << sol[i] << " "; 
	cout << endl;
	return 0;
	
}