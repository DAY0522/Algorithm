// 숫자의 개수
// https://www.acmicpc.net/problem/2577

#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int num, result = 1;
	for (int i = 0; i < 3; i++){
		cin >> num;
		result *= num;
	}

	vector<int> v(10, 0);
	while (result > 0) {
		v[result % 10]++;
		result /= 10;
	}

	for (int i = 0; i < 10; i++) cout << v[i] << '\n';

	return 0;
}