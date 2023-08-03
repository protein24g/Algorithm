#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int i, A, B, C;
    int ary[10] = {};
    cin >> A >> B >> C;
    int res = A * B * C;
    string s1 = to_string(res);
    for(i = 0; i<s1.length(); i++) ary[s1[i] - '0']++;
    for(i = 0; i<10; i++) cout << ary[i] << "\n";
        
    return 0;
}