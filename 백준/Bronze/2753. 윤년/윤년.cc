#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n;
    cin >> n;
    if(n % 4 == 0 and n % 100 != 0 or n % 400 == 0) cout << "1";
    else cout << "0";
    return 0;
}