#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    long long w, h, n;
    cin >> w >> h >> n;
    
    long long left = -1;
    long long right = max(w, h) * n;
    
    while (right - left > 1) {
        long long mid = left + (right - left) / 2;
        
        long long count_w = mid / w;
        long long count_h = mid / h;
        
        if (count_w == 0 or count_h == 0) {
            left = mid;
        } 
        else if (count_w >= (n + count_h - 1) / count_h) { 
            right = mid;
        } else {
            left = mid;
        }
    }
    cout << right;
    return 0;
}