#include <iostream>
#include <cmath>

using namespace std;

double f(int a, int b, int c, int d, double x){
    return a*x*x*x + b*x*x + c*x + d;
}

int main()
{   
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    double left = -2000.0;
    double right = 2000.0;
    
    for (int i = 0; i < 1000; i++) {
        double mid = left + (right - left) / 2;
        if (f(a, b, c, d, left)*f(a, b, c, d, mid) > 0) {
            left = mid;
        } else {
            right = mid;
        }
    }

    cout.setf(ios::fixed); 
    cout.precision(4);

    cout << right << endl;

    return 0;
}