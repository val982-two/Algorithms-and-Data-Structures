#include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& arr, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (arr[j + 1] > arr[j]){
                swap(arr[j + 1], arr[j]);
            }
        }
    }
}


int main(){
    vector<int> arr;
    int x;

    while (cin >> x){
        arr.push_back(x);
    }
    int n = arr.size();
    BubbleSort(arr, n);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}