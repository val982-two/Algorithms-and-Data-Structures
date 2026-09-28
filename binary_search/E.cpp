#include <iostream>
#include <vector>

using namespace std;

bool good(vector<int>& boxes, int k, int r){
    int cows_count = 1;
    int pre_box = boxes[0];
    for (int i = 1; i < boxes.size(); i++) {
        if ((boxes[i] - pre_box) >= r) {
            cows_count++;
            pre_box = boxes[i];
        }
    }
    return cows_count >= k;
}

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> arr;
    int a;
    for (int i = 0; i < N; i++){
        cin >> a;
        arr.push_back(a);
    }

    int left = -1;
    int right = arr.back() - arr[0] + 1;

    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (good(arr, K, mid)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    cout << left << endl;
    
    
    
    return 0;
}