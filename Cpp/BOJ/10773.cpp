// 10773¹ø Á¦·Î
// https://www.acmicpc.net/problem/10773

#include <iostream>
#include <stack>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int K;
	cin >> K;

	stack<int> s;
	while (K--) {
		int num;
		cin >> num;

		if (num) s.push(num);
		else s.pop();
	}

	int result = 0;
	while (s.size()) {
		result += s.top();
		s.pop();
	}

	cout << result;

	return 0;
}