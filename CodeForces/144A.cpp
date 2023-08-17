#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(x, to) for(x=0; x<(to); x++)
#define FOR_DECREMENT(x,to) for(x; x>to; x--)
#define ARR_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))
#define PB push_back

int main() {

    int n;
    cin >> n;
    vector<int> v(n);
    int i;
    FOR(i, v.size()) {
        cin >> v[i];
    }

    int minIndex = distance(v.begin(), min_element(v.begin(), v.end()));
    cout << "minIndex: " << minIndex << endl;
    int count = 0;
    for (int i = minIndex; i < v.size() - 1; i++) {
        swap(v[i], v[i + 1]);
        count++;
    }
    cout << count << endl;

    int maxIndex = distance(v.begin(), max_element(v.begin(), v.end()));
    cout << "maxIndex: " << maxIndex << endl;
    count = 0;  // Reset count to 0
    FOR_DECREMENT(maxIndex, i) {
        swap(v[maxIndex], v[maxIndex - 1]);
        count++;
    }
    cout << count << endl;

    return 0;
}
