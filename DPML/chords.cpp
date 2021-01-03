#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;
#define LM 7
#define NM 16

// Variables related to diatonic and chromatic notes absolute position
map <string, double> note_pos;
map <double, string> pos_note;
int notes_num;
int L1 = 6;

// Variables related to the C Major scale steps and harmonic chords
vector <string> c_major_step;
vector <string> c_major_ch;
int c_major_num;
int L2 = 7;

// Variables related to chords and the notes they consist of
map <string, vector<string> > chord_notes;
vector <string> common_notes[LM][LM];

// Variables related to backtracking and search
int sol[NM];
int num_sol = 100;
int total_sol;

double double_mod(double num, int m) {
	int inum = int(num);
	double rem = num - inum;
	return (inum % m) + rem;
}

void read_input() {
	ifstream cin1("note_pos.in");
	ifstream cin2("c_major_ch.in");

	cout << "\n" << "1. Diatonic & chromatic notes mapped to their absolute position" << "\n\n";
	cin1 >> notes_num;
	for (int i = 0; i < notes_num; ++i) {
		string note; double pos;
		cin1 >> note >> pos;
		cout << note << " " << pos << "\n";
		note_pos[note] = pos;
		pos_note[pos] = note;
	}

	cout << "\n" << "2. Chords (& roots) in C Major scale" << "\n\n";
	cin2 >> c_major_num;
	for (int i = 0; i < c_major_num; ++i) {
		string step;
		cin2 >> step;
		c_major_step.push_back(step);
	}
	for (int i = 0; i < c_major_num; ++i) {
		string chord;
		cin2 >> chord;
		c_major_ch.push_back(chord);
	}
	for (int i = 0; i < c_major_ch.size(); ++i)
		cout << c_major_ch[i] << "\n";
}

void create_chords() {
	cout << "\n" << "3. Chord notes (root, third & fifth)" << "\n\n";
	for (int i = 0; i < c_major_num; ++i) {
		cout << c_major_ch[i] << "\n";
		vector <string> ch_notes;
		ch_notes.push_back(c_major_step[i]);			// Add root
		ch_notes.push_back(c_major_step[(i+2) % L2]);	// Add third
		ch_notes.push_back(c_major_step[(i+4) % L2]);	// Add fifth
		for (int j = 0; j < ch_notes.size(); ++j) cout << ch_notes[j] << " ";
		cout << "\n";
		chord_notes[c_major_ch[i]] = ch_notes;
	}
}

void establish_relations() {
	cout << "\n" << "4. Establish relations between C Major scale harmonic chords" << "\n\n";
	for (int i = 0; i < c_major_num; ++i)
		for (int j = 0; j < c_major_num; ++j){
			string ch_1 = c_major_ch[i];
			string ch_2 = c_major_ch[j];
			for (int k = 0; k < chord_notes[ch_1].size(); ++k)
				for (int l = 0; l < chord_notes[ch_2].size(); ++l)
					if (chord_notes[ch_1][k] == chord_notes[ch_2][l]) 
						common_notes[i][j].push_back(chord_notes[ch_1][k]);
		}

	for (int i = 0; i < c_major_num; ++i)
		for (int j = 0; j < c_major_num; ++j){
			string ch_1 = c_major_ch[i];
			string ch_2 = c_major_ch[j];
			cout << ch_1 << " and " << ch_2 << ": ";
			for (int k = 0; k < common_notes[i][j].size(); ++k)
				cout << common_notes[i][j][k] << " ";
			cout << "\n";
		}
}

int valid(int min_nc, int max_nc, int length) {
	for (int i = 1; i < length; ++i) {
		int c1 = sol[i-1];
		int c2 = sol[i];
		if (common_notes[c1][c2].size() < min_nc || common_notes[c1][c2].size() > max_nc) return 0;
	}
	return 1;
}

void print_sol(int length) {
	for (int i = 0; i < length; ++i) {
		string ch = c_major_ch[sol[i]];
		cout << ch << " ";
	}
	cout << "\n";
}

void generate(int pos, int min_nc, int max_nc, int length) {
	if (pos == length - 1) {
		if (valid(min_nc, max_nc, length)) {
			total_sol++;
			print_sol(length);
		}
		return;
	}
	for (int i = 0; i < c_major_num; ++i) {
		sol[pos] = i;
		generate(pos + 1, min_nc, max_nc, length);
		if (total_sol >= num_sol) return;
	}
}

// C Major scale chord progression generator
// start/end: starting/ending chord index (eg. 0 for C, 1 for D...)
// min_nc/max_nc: how many notes should 2 successive chords have in common
// length: the length of the chords progression
void generate_chords(int start, int end, int min_nc, int max_nc, int length) {
	sol[0] = start;
	sol[length - 1] = end;
	generate(1, min_nc, max_nc, length);
}

int main() {
	// Test double mod
	// cout << double_mod(7.75, L1) << "\n";
	read_input();
	create_chords();
	establish_relations();
	total_sol = 0;
	cout << "\n" << "Various starts, various num common notes exact" << "\n\n";
	generate_chords(2, 2, 0, 0, 8); // 0 common notes progression from E
	total_sol = 0;
	generate_chords(0, 0, 1, 1, 8); // 1 common note progression from C
	total_sol = 0;
	generate_chords(1, 1, 2, 2, 8); // 2 common notes progression from D
	cout << "\n" << "All from C, various num common notes exact" << "\n\n";
	total_sol = 0;
	generate_chords(0, 0, 0, 0, 8); // 0 common notes progression from E
	total_sol = 0;
	generate_chords(0, 0, 1, 1, 8); // 1 common note progression from C
	total_sol = 0;
	generate_chords(0, 0, 2, 2, 8); // 2 common notes progression from D

	return 0;
}