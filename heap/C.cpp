#include <iostream>
#include <vector>
#include <string>

class MinHeap {
private:
    std::vector<long long> heap;
    int size;

    void shiftUp(int i) {
        while (i / 2 > 0 && heap[i] < heap[i / 2]) {
            std::swap(heap[i], heap[i / 2]);
            i /= 2;
        }
    }

    int indMinChild(int i) {
        if (i * 2 + 1 > size) {
            return 2 * i;
        }
        if (heap[2 * i] < heap[2 * i + 1]) {
            return 2 * i;
        }
        return 2 * i + 1;
    }

    void shiftDown(int i) {
        while (2 * i <= size) {
            int j = indMinChild(i);
            if (heap[i] > heap[j]) {
                std::swap(heap[i], heap[j]);
                i = j;
            } else {
                break;
            }
        }
    }

public:
    MinHeap() : size(0) {
        heap.push_back(0);
    }

    void add(long long x) {
        heap.push_back(x);
        size++;
        shiftUp(size);
    }

    bool extract(long long &result) {
        if (size == 0) {
            return false;
        }
        result = heap[1];
        heap[1] = heap[size];
        size--;
        heap.pop_back();
        shiftDown(1);
        return true;
    }

    void clear() {
        heap.clear();
        heap.push_back(0);
        size = 0;
    }

    bool empty() const {
        return size == 0;
    }
};

int main() {
    MinHeap heap;
    std::string command;

    while (std::cin >> command) {
        if (command == "ADD") {
            long long x;
            std::cin >> x;
            heap.add(x);
        } else if (command == "EXTRACT") {
            long long val;
            if (heap.extract(val)) {
                std::cout << val << "\n";
            } else {
                std::cout << "CANNOT\n";
            }
        } else if (command == "CLEAR") {
            heap.clear();
        }
    }

    return 0;
}