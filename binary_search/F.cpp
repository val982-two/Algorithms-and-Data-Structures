#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int f(int t, int x, int y) {
    int t_first = min(x, y);
    if (t < t_first) {return 0;}
    int sheet_copy = 1 + (t - t_first) / x + (t - t_first) / y;

    return sheet_copy;
}

int main()
{
    int n, x, y;
    cin >> n >> x >> y;

    int left = -1;
    int right = 2e9;

    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (f(mid, x, y) >= n) {
            right = mid;
        } else {
            left = mid;
        }
    }
    
    cout << right;
    
    return 0;
}