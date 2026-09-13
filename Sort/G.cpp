#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& arr, int n)
{
    vector<int> temp(101, 0);

    for (int i = 0; i < n; i++)
    {
        temp[arr[i]]++;
    }

    int index = 0;
    for (int number = 0; number < 101; number++)
    {
        for (int k = 0; k < temp[number]; k++)
        {
            arr[index] = number;
            index++;
        }
    }

}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x)
    {
        arr.push_back(x);
    }
    
    int n = arr.size();
    CountSort(arr, n);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}
