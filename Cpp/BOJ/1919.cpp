// 1919번 애너그램 만들기
// https://www.acmicpc.net/problem/1919

#include <iostream>
using namespace std;

int main() {
	string A, B;
	int arr[26] = {};

	cin >> A >> B;
	for (auto c : A) arr[c - 'a']++;
	for (auto c : B) arr[c - 'a']--;

	int cnt = 0;
	for (int i : arr) cnt += abs(i);
	cout << cnt;

	return 0;
}