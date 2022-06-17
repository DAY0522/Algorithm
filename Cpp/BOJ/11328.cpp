// 11328¹ø Strfry
// https://www.acmicpc.net/problem/11328

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;
	while (N--) {
		int arr[26] = {};
		string A, B;
		cin >> A >> B;
		for (auto c : A) arr[c - 'a']++;
		for (auto c : B) arr[c - 'a']--;

		bool result = true;
		for (int i : arr) if (i != 0) result = false;

		if (result) cout << "Possible\n";
		else cout << "Impossible\n";
	}

	return 0;
}