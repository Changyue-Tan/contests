// suppose to have bug, cannot find it 
// do not what is the test case to involk the bug

#include <iostream>
#include <set>
using namespace std;

set<int> ropes; // or unordered_set

int main(void) {
    int n;
    int target;
    cin >> n >> target;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        ropes.insert(t);
    }

    for (int a : ropes) {
        int b = target - a;
        if (ropes.count(b)) {
            cout << "YES\n" << a << ' ' << b << '\n';
            return 0;
        }
    }

    cout << "NO\n";
}
