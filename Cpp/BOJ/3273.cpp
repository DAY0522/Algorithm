// �� ���� ��
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

// �ð� ������ �־ ���Ʈ������ ���� ���� ��?
// �տ��� �� ���� �ִ���, �������� ����. ���Ŀ� x���� ���� �ε����� ���� �� ���� �տ��� �־�����,
// ���� �ϳ� ���� ���̴�.
// ���� �ٸ� ���� ������.... ��ġ�� ��찡 ���ڱ���...?