#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int j, i, ary[4];
    
    for(j=0; j<3; j++){
        int cnt = 0;
        for(i=0; i<4; i++){
            cin >> ary[i];
            if (ary[i] == 0) cnt++;
        }
        if (cnt == 1) cout << "A\n";
        else if (cnt == 2) cout << "B\n";
        else if (cnt == 3) cout << "C\n";
        else if (cnt == 4) cout << "D\n";
        else cout << "E\n";
    }
    return 0;
}