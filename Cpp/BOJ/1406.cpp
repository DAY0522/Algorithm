// 1406번 에디터
// https://www.acmicpc.net/problem/1406

// 야매 연결리스트 구현을 통해서도 풀어보자!

#include <iostream>
#include <list>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string str;
	cin >> str;

	list<char> L;
	for (auto c : str) {
		L.push_back(c);
	}

	int N;
	cin >> N;
	auto cursor = L.end();
	while(N--){
		char c;
		cin >> c;
		if (c == 'L') {
			if (cursor != L.begin()) cursor--;
		}
		else if (c == 'D') {
			if (cursor != L.end()) cursor++;
		}
		else if (c == 'B') {
			if (cursor != L.begin()) {
				cursor--;
				cursor = L.erase(cursor); // 이미 할당이 해제된 주소를 가리키면 안 되므로, 반환값인 cursor의 다음 값을 할당
			}
		}
		else {
			char add;
			cin >> add;
			L.insert(cursor, add);
		}
	}

	for (auto c : L) cout << c;
}