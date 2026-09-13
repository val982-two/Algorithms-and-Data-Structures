#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& arr, int n) {
    for (int i = 0; i < n - 1; i++){
        for (int j = i + 1; j < n; j++){
            if (arr[i] <= arr[j]){
                swap(arr[i], arr[j]);
            }
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
    SelectionSort(arr, n);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}