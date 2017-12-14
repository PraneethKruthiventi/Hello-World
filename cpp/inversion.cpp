#include <bits/stdc++.h>
using namespace std;
int ans;
void merge(int input_array[], int start, int mid, int end)
{
	int p = start, q = mid+1, k=0, i;
	int A[end-start+1];
	for(i=start; i<=end; i++)
	{
		if(p > mid)
			A[k++] = input_array[q++];
		else if(q > end)
			A[k++] = input_array[p++];
		else if(input_array[p] < input_array[q])
			A[k++] = input_array[p++];
		else
		{
			A[k++] = input_array[q++];
			ans += mid-p+1;
		}
	}
	for(i=0; i<k; i++)
		input_array[start++] = A[i];
}

void inversions(int input_array[], int start, int end)
{
	if(start < end)
	{
		int mid = (start + end)/2;
		inversions(input_array, start, mid);
		inversions(input_array, mid+1, end);
		merge(input_array, start, mid, end);
	}
}
int main()
{
	int n, i;
	cin >> n;
	int input_array[n];
	for(i=0; i<n; i++)
		cin >> input_array[i];
	//for(i=0; i<n; i++)
	//	cout << input_array[i] << " ";
	//cout << endl <<"*****" << endl;
	inversions(input_array, 0, n-1);
	cout << ans << endl;
	return 0;	
}