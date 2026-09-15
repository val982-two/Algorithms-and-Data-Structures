#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[min_idx]) {
                min_idx = j;
            }
        }
        swap(arr[i], arr[min_idx]);
    }
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }

    int n = arr.size();
    SelectionSort(arr, n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}