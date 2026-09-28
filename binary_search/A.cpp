#include <iostream>
#include <vector>

using namespace std;

int binary_search(vector<int>& arr, int n, int x) {
    int left = -1;
    int right = n;
    int mid;
    while (right - left > 1){
        mid = left + (right - left) / 2;
        if (x <= arr[mid]){
            right = mid;
        } else {
            left = mid;
        }
    }
    if (right < n and x == arr[right]){
        return 1;
    }
    return 0;
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
        if (binary_search(A, N, B[i]) == 1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}