// 1158�� �似Ǫ�� ����
// https://www.acmicpc.net/problem/1158

// list�� �� �� list.end()�� NULL�̴�.
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

	auto p = L.begin(); // ������ �� ������(1)

	cout << "<";
	while (L.size()) { // L�� ũ�Ⱑ 1�̸� ����(0�� �������� ��)
		for (int i = 0; i < K-1; i++) { // erase���� p�� �� �� �Ѱ��ֹǷ� K-1�� �����ϰ� ��.
			if (p == L.end()) p = L.begin();
			p++;
		}

		if (p == L.end()) p = L.begin();

		cout << *p;
		if (L.size() != 1) cout << ", ";
		
		p = L.erase(p); // erase �������� ���� ����Ʈ�� �Ѱ��ֹǷ� for���� K-1ȸ�� �����ϰ� ��.
		if (p == L.end()) p = L.begin();
	}
	cout << ">";

	return 0;
}