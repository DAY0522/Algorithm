// 1406�� ������
// https://www.acmicpc.net/problem/1406

// �߸� ���Ḯ��Ʈ ������ ���ؼ��� Ǯ���!

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
				cursor = L.erase(cursor); // �̹� �Ҵ��� ������ �ּҸ� ����Ű�� �� �ǹǷ�, ��ȯ���� cursor�� ���� ���� �Ҵ�
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