// 5397�� Ű�ΰ�
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
					cursor--; // �� �κ��� ����? �� �ؾ��ϴ���? -> cursor�� ������� ���� �� ĭ �ڸ� ����Ŵ
					cursor = L.erase(cursor); // �̷��� �ϸ� cursor�� �̹� ������ ���� ����Ű�� ���̹Ƿ�, ���� �ɷ� �ٲ���
				}
			}
			else {
				L.insert(cursor, c); // insert �� Ŀ���� insert�� ���� �ڸ��� ����Ŵ(curosr �ڸ��� �״�γ� �տ� ���� �߰��� �� ����)
			}
 		}
		for (auto c : L) cout << c;
		cout << '\n';
	}

	return 0;
}