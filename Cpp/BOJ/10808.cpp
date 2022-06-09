// https://www.acmicpc.net/problem/10808

#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    for (char a = 'a'; a <= 'z'; a++){
        int cnt = 0;
        for (auto c : s) {
            if (a == c) cnt++;
        }
        cout << cnt << ' ';
    }
}


//int main(void) {
//    ios::sync_with_stdio(0);
//    cin.tie(0);
//    string s;
//    cin >> s;
//
//    vector<int> v(26, 0);
//    for (auto c : s) {
//        v[c - 'a']++;
//    }
//
//    for (int i = 0; i < 26; i++)
//    {
//        cout << v[i] << ' ';
//    }
//}