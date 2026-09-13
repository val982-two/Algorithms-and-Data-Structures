#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int partition(vector<int>& arr, int left, int right){
    int random_pivot = left + rand() % (right - left + 1);
    swap(arr[random_pivot], arr[right]);
    
    int pivot = arr[right];
    int i = left;

    for (int j = left; j < right; j++){
        if (arr[j] < pivot){
            swap(arr[i], arr[j]);
            i++;
        } 
    }
    swap(arr[i], arr[right]);
    return i;
}

void QuickSort(vector<int>& arr, int left, int right){
    if (left < right){
        int p = partition(arr, left, right);
        QuickSort(arr, left, p - 1);
        QuickSort(arr, p + 1, right);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int left = 0;
    int right = n - 1;

    QuickSort(arr, left, right);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}