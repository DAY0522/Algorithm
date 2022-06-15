// 13300번 방 배정
// https://www.acmicpc.net/problem/13300

#include <iostream>
#include <cmath>
using namespace std;

int arr[13];

int main() {
	int S, Y, N, K;
	int cnt = 0;
	cin >> N >> K;
	for (int i = 0; i < N; i++){
		cin >> S >> Y;
		arr[2 * (Y - 1) + S]++;
	}

	for (int i = 0; i < 12; i++){
		cnt += floor(float(arr[i] - 1) / K) + 1;
	}
	cout << cnt;

	return 0;
}