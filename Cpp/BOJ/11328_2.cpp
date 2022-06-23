// 11328¹ø Strfry
// https://www.acmicpc.net/problem/11328

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string A, B;
	int N;
	cin >> N;
	while (N-- > 0) {
		cin >> A >> B;
		sort(A.begin(), A.end());
		sort(B.begin(), B.end());
		if (A.compare(B)) cout << "Impossible\n";
		else cout << "Possible\n";
	}

	return 0;
}