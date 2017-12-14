#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--)
    {
	    int n, m, x, y;
	    cin >> n >> m;
        int div = n/m;
        if(div > 0)
        {x = div, y = div+1;}
        else
        {x = div, y = div-1;}
        x = x*m; y = y*m;
        if(abs(abs(x)-abs(n)) > abs(abs(y)-abs(n)))
            cout << y << endl;
        else if(abs(abs(x)-abs(n)) == abs(abs(y)-abs(n)))
            if(abs(x) > abs(y))
                cout << x << endl;
            else
                cout << y << endl;
        else
            cout << x << endl;    
    }
return 0;	
}