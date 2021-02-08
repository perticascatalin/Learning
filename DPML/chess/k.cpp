#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <vector>

using namespace std;
#define NM 10

int N;
int mark[NM][NM];
int pl[8] = {-1,-2,-2,-1,1,2,2,1};
int pc[8] = {-2,-1,1,2,2,1,-1,-2};
int found, num_sol;
vector <int> sol;

// Displays the board: each cell value shows the step at which it was reached
void display_solution() {
	int display[NM][NM];
	memset(display, 0, sizeof(display));
	for (int i = 0; i < N * N; ++i) {
		int loc = sol[i];
		int l = loc / N;
		int c = loc % N;
		display[l][c] = i + 1;
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) cout << display[i][j] << " ";
		cout << "\n";
	}
	cout << "\n";
}

// Explore subtree at level step
void explore(int step) {
	if (step == N * N) { // We have a solution, print it & return
		++found;
		display_solution();
		return;
	}
	int loc = sol[step - 1];
	int l = loc / N;
	int c = loc % N;
	for (int k = 0; k < 8; ++k) {
		int nl = l + pl[k];
		int nc = c + pc[k];
		// A move is not allowed if outside the board or marked cell
		if (nl < 0 || nl >= N) continue;
		if (nc < 0 || nc >= N) continue;
		if (mark[nl][nc]) continue;

		mark[nl][nc] = 1;
		sol.push_back(N * nl + nc);
		explore(step + 1);
		sol.pop_back();
		mark[nl][nc] = 0;
		if (found == num_sol) return;
	}
}

int main() {
	int l, c;
	ifstream cin("k.in");
	cin >> N >> l >> c >> num_sol;
	clock_t begin = clock();
	memset(mark, 0, sizeof(mark));
	mark[l][c] = 1;
	sol.push_back(N * l + c);
	found = 0;
	explore(1);
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "Time (sec): " << elapsed_secs << "\n";
	cout << "Solutions found: " << found << "\n";
	return 0;
}