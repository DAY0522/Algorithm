// 10807번 개수 세기
// https://www.acmicpc.net/problem/10807

#include <iostream>
using namespace std;

int N, v, cnt;
int arr[101];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	cin >> v;

	for (int i = 0; i < N; i++)
	{
		if (arr[i] == v) cnt++;
	}

	cout << cnt;

	return 0;
}