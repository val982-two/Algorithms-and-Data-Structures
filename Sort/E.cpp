#include <iostream>
#include <vector>

using namespace std;

void Merge(vector<int>& arr ,int left, int mid, int right){
    vector<int> temp;
    int i = left;
    int j = mid + 1;

    while (i <= mid and j <= right) {
        if (arr[i] <= arr[j]) {
            temp.push_back(arr[i]);
            i++;
        } else {
            temp.push_back(arr[j]);
            j++;
        }
    }

    while (i <= mid){
        temp.push_back(arr[i]);
        i++;
    }

    while (j <= right){
        temp.push_back(arr[j]);
        j++;
    }

    for (int k = 0; k < temp.size(); k++){
        arr[left + k] = temp[k];
    }
}

void MergeSort(vector<int>& arr, int left, int right){
    if (left >= right){
        return;
    }
    int mid = left + (right - left) / 2;

    MergeSort(arr, left, mid);
    MergeSort(arr, mid + 1, right);

    Merge(arr, left, mid, right);
}

int main(){
    vector<int> arr;
    int n;
    cin >> n;
    int a;
    for (int i = 0; i < n; i++){
        cin >> a;
        arr.push_back(a);
    }
    int left = 0;
    int right = n - 1;

    MergeSort(arr, left, right);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}