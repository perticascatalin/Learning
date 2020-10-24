#include <iostream>
#include <fstream>
#include <string>
#include <vector>
	
using namespace std;
#define NM 1005

int N, M;
int A[NM][NM], B[NM][NM];
int marked[NM];
vector<int> G[NM];
vector<int> CT[NM];

int main()
{
	ifstream cin("ctc.in");
	ofstream cout("ctc.out");
	memset(A, 0, sizeof(A));
	memset(B, 0, sizeof(B));
	memset(marked, 0, sizeof(marked));

	cin >> N >> M;
	if (N > 1000) return 0;
	for (int i = 0; i < M; ++i)
	{
		int a, b;
		cin >> a >> b;
		G[a].push_back(b);
		A[a][b] = 1;
		B[a][b] = 1;
	}

	// for (int i = 1; i <= N; ++i)
	// {
	// 	for (int j = 1; j <= N; ++j) cout << A[i][j] << " ";
	// 	cout << "\n";
	// }

	for (int k = 1; k <= N; ++k)
		for (int i = 1; i <= N; ++i)
				for (int j = 1; j <= N; ++j)
					if (B[i][k] && B[k][j]) B[i][j] = 1;

	int num_ctc = 0;
	for (int i = 1; i <= N; ++i)
		if (!marked[i])
		{
			++num_ctc;
			CT[num_ctc].push_back(i);
			marked[i] = 1;
			for (int j = 1; j <= N; ++j)
				if (!marked[j] && B[i][j] && B[j][i])
				{
					CT[num_ctc].push_back(j);
					marked[j] = 1;
				}
		}
	cout << num_ctc << "\n";
	for (int i = 1; i <= num_ctc; ++i)
	{
		for (int j = 0; j < CT[i].size(); ++j)
			cout << CT[i][j] << " ";
		cout << "\n";
	}
	return 0;
}