// 1874번 스택 수열
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
		num = q.front(); // pop 해야되는 원소 추출

		while (num >= cnt) { // pop 하려는 게 아직 push되지 않은 경우 -> push
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