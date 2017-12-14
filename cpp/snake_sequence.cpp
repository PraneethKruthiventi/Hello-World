#include <iostream>
using namespace std;
//can move right and down
int main()
{
	long long int n;
	cin >> n;
	long long int value[n][n];
	long long int length[n][n] = {{0}};

	long long temp_left, temp_up, temp_length = 0;
	//input
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> value[i][j];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			length[i][j] = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			//check left and up
			if(i != 0 && j != 0)
			{
				temp_left = value[i][j] - value[i][j-1]; 
				if(temp_left == 1 || temp_left == -1)
					length[i][j] = length[i][j-1] + 1;
				temp_up = value[i][j] - value[i-1][j];
				if(temp_up == 1 || temp_up == -1)
					length[i][j] = max(length[i][j], length[i-1][j] + 1);
			}
			//check up
			else if (i != 0 && j == 0)
			{
				temp_up = value[i][j] - value[i-1][j];
				if(temp_up == 1 || temp_up == -1)
					length[i][j] = length[i-1][j] + 1;
			}
			//check left
			else if (i == 0 && j != 0)
			{
				temp_left = value[i][j] - value[i][j-1]; 
				if(temp_left == 1 || temp_left == -1)
					length[i][j] = length[i][j-1] + 1;
			}
			else
			{
				length[i][j] = 0;
			}
			temp_length = max(temp_length, length[i][j]);
		}
	}
	cout << temp_length;
	
	return 0;
}
