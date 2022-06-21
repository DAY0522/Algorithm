// 5397번 키로거
// https://www.acmicpc.net/problem/5397

#include <iostream>
#include <list>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	while (N--) {
		string str;
		cin >> str;

		list<char> L;
		auto cursor = L.begin();

		for (auto c : str) {
			if (c == '<') {
				if (cursor != L.begin()) cursor--;
			}
			else if (c == '>') {
				if (cursor != L.end()) cursor++;
			}
			else if (c == '-') {
				if (cursor != L.begin()) {
					cursor--; // 이 부분의 역할? 왜 해야하는지? -> cursor는 지우려는 것의 한 칸 뒤를 가리킴
					cursor = L.erase(cursor); // 이렇게 하면 cursor는 이미 지워진 값을 가리키는 것이므로, 다음 걸로 바꿔줌
				}
			}
			else {
				L.insert(cursor, c); // insert 시 커서는 insert된 다음 자리를 가리킴(curosr 자리는 그대로나 앞에 무언가 추가만 된 것임)
			}
 		}
		for (auto c : L) cout << c;
		cout << '\n';
	}

	return 0;
}