// ¹æ ¹øÈ£
// https://www.acmicpc.net/problem/1475

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;

	int arr[10] = {0,};
	while (N) {
		arr[N % 10]++;
		N /= 10;
	}

	arr[6] += arr[9];
	arr[6] = ceil(float(arr[6]) / 2);
	arr[9] = 0;

	cout << *max_element(arr, arr+10);

	return 0;
}