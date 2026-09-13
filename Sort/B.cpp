#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& arr, int n){
    for (int i = 1; i < n; i++){
        for (int j = i; j > 0 and arr[j - 1] >= arr[j]; j--){
            swap(arr[j - 1], arr[j]);
        }
    }
}

int main() {
    vector<int> arr;
    int x;

    while (cin >> x){
        arr.push_back(x);
    }
    int n = arr.size();
    InsertionSort(arr, n);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

    return 0;
}