#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0); cin.tie(0);
    int i, N, X, A;
    cin >> N >> X;
    for(i=0; i<N; i++){
        cin >> A;
        if (A < X) cout << A << " ";
    }
    
    return 0;
}
