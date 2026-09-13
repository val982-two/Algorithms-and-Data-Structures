#include <iostream>
#include <vector>

using namespace std;
int k = 0;
void BubbleSort(vector<int>& arr, int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (arr[j + 1] < arr[j]){
                swap(arr[j + 1], arr[j]);
                k += 1;
            }
        }
    }
}


int main(){
    int n;
    cin >> n;
    vector<int> arr;
    int a;

    for (int i = 0; i < n; i++){
        cin >> a;
        arr.push_back(a);
    }
    BubbleSort(arr, n);
    cout << k << endl;
    return 0;
}