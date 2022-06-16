// 1874�� ���� ����
// https://www.acmicpc.net/problem/1874

#include <iostream>
#include <queue>
#include <stack>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, cnt = 1;
	int num, pop;
	queue<int> q;
	queue<char> ans;
	stack<int> s;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		q.push(num);
	}

	while (q.size()) {
		num = q.front(); // pop �ؾߵǴ� ���� ����

		while (num >= cnt) { // pop �Ϸ��� �� ���� push���� ���� ��� -> push
			s.push(cnt++);
			ans.push('+');
		}

		if (s.top() != q.front())
		{
			cout << "NO";
			return 0;
		}
		q.pop();
		s.pop();
		ans.push('-');
	}

	while (ans.size())
	{
		cout << ans.front() << '\n';
		ans.pop();
	}

	return 0;
}