#include <iostream>
#include <cmath>

using namespace std;

double f(double x){
    return x*x + sqrt(x);
}

int main()
{
    double c;
    cin >> c;

    double left = 0.0;
    double right = sqrt(c);

    for (int i = 0; i < 100; i++){
        double mid = left + (right - left) / 2;
        if (f(mid) > c) {
            right = mid;
        } else {
            left = mid;
        }
    }
    cout.setf(ios::fixed); 
    cout.precision(6);

    cout << right << endl;

    return 0;
}