// suppose to have bug, cannot find it 
// do not what is the test case to involk the bug -- edit: found the bug after proper testing


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
        // if (ropes.count(b)) {
        // will fail in test case:
        // in:  3 40
        //      10 20 40
        // out: NO
        if (ropes.count(b) && b != a) {
            cout << "YES\n" << a << ' ' << b << '\n';
            return 0;
        }
    }

    cout << "NO\n";
}
