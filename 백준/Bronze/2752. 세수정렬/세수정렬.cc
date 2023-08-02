#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int i, ary[3];
    for(i=0; i<sizeof(ary)/4; i++) cin >> ary[i];
    sort(ary, ary+sizeof(ary)/4);
    for(i=0; i<sizeof(ary)/4; i++) cout << ary[i] << " ";
    return 0;
}