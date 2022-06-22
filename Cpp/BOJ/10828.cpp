// 10828¹ø ½ºÅÃ
// https://www.acmicpc.net/problem/10828

#include <iostream>
#include <stack>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	stack<int> stack;


	cin >> N;
	while (N--) {
		string s;
		cin >> s;
		if (s == "push") {
			int n;
			cin >> n;
			stack.push(n);
		}
		else if (s == "pop") {
			if (stack.empty()) cout << -1 << "\n";
			else {
				cout << stack.top() << "\n";
				stack.pop();
			}
		}
		else if (s == "size") cout << stack.size() << "\n";
		else if (s == "empty") {
			if (stack.empty()) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
		else {
			if (stack.empty()) cout << -1 << "\n";
			else cout << stack.top() << "\n";
		}
	}

	return 0;
}