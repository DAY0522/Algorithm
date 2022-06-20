// 1158번 요세푸스 문제
// https://www.acmicpc.net/problem/1158

// list의 맨 뒤 list.end()는 NULL이다.
#include <iostream>
#include <list>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, K;
	cin >> N >> K;

	list<int> L = {};
	for (int i = 1; i <= N; i++){
		L.push_back(i);
	}

	auto p = L.begin(); // 시작은 맨 앞지점(1)

	cout << "<";
	while (L.size()) { // L의 크기가 1이면 종료(0만 남아있을 때)
		for (int i = 0; i < K-1; i++) { // erase에서 p를 한 번 넘겨주므로 K-1만 동작하게 함.
			if (p == L.end()) p = L.begin();
			p++;
		}

		if (p == L.end()) p = L.begin();

		cout << *p;
		if (L.size() != 1) cout << ", ";
		
		p = L.erase(p); // erase 과정에서 다음 포인트를 넘겨주므로 for문은 K-1회만 동작하게 함.
		if (p == L.end()) p = L.begin();
	}
	cout << ">";

	return 0;
}