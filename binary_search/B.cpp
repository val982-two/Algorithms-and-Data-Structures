#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int binary_search(vector<int>& arr, int n, int x)
{
    int left = -1;
    int right = n;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (x >= arr[mid]) {
            left = mid;
        } else {
            right = mid;
        }
    }
    if (left == -1) {return arr[right];}
    if (right == n) {return arr[left];}

    if (abs(arr[left] - x) <= abs(arr[right] - x)) {
        return arr[left];
    }
    return arr[right];
    
}

int main()
{
    int N;
    int K;
    cin >> N >> K;

    vector<int> A;
    vector<int> B;

    int a;
    for (int i = 0; i < N; i++){
        cin >> a;
        A.push_back(a);
    }
    for (int i = 0; i < K; i++){
        cin >> a;
        B.push_back(a);
    }

    for (int i = 0; i < K; i++){
        cout << binary_search(A, N, B[i]) << endl;
    }
    return 0;
}