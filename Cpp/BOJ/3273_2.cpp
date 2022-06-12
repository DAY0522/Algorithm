// 두 수의 합
// https://www.acmicpc.net/problem/3273

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, x;
	cin >> n;

	int* arr = new int[n];
	for (int i = 0; i < n; i++) cin >> arr[i];
	cin >> x;

	sort(arr, arr + n);
	
	int l = 0, r = n - 1;
	int cnt = 0;

	while (l < r) {
		int sum = arr[l] + arr[r];
		if (sum < x) l++;
		else if (sum > x) r--;
		else {
			l++;
			r--;
			cnt++;
		}
	}
	cout << cnt;

	return 0;
}