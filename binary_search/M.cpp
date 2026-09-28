#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> ropes;
    int a;
    for (int i = 0; i < n; i++){
        cin >> a;
        ropes.push_back(a);
    }
    
    int left = 0;
    int right = 1e8;
    
    while (right - left > 1) {
        long long count = 0;
        int mid = left + (right - left) / 2;
        for (int i = 0; i < n; i++) {
            count += ropes[i] / mid;
        }
        if (count >= k) {
            left = mid;
        } else {
            right = mid;
        }
    }
    cout << left;
    return 0;
}