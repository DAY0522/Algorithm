// 두 수의 합
// https://www.acmicpc.net/problem/3273

#include <iostream>
using namespace std;

int arr[1000001] = {};
bool cnt[2000001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, x, result = 0;
	cin >> n;
	for (int i = 0; i < n; i++)	cin >> arr[i];
	cin >> x;

 	for (int i = 0; i < n; i++){
		if (x - arr[i] > 0 && cnt[x - arr[i]]) result++;
		cnt[arr[i]] = 1;
	}
	cout << result;

	return 0;
}

// 시간 제한이 있어서 브루트포스는 조금 힘들 듯?
// 앞에서 그 수가 있는지, 없는지를 센다. 이후에 x에서 현재 인덱스의 값을 뺀 값이 앞에서 있었으면,
// 쌍이 하나 느는 것이다.
// 서로 다른 양의 정수네.... 겹치는 경우가 없겠구나...?