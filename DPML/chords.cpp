#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

map <string, double> ch_pos;
map <double, string> pos_ch;
int ch_num;
int L1 = 6;

vector <string> c_major_step;
vector <string> c_major_ch;
int c_major_num;
int L2 = 7;

map <string, vector<string> > chord_notes;

double double_mod(double num, int m) {
	int inum = int(num);
	double rem = num - inum;
	return (inum % m) + rem;
}

void read_input() {
	ifstream cin1("ch_pos.in");
	ifstream cin2("c_major_ch.in");

	cout << "\n" << "1. Diatonic & chromatic notes mapped to their absolute position" << "\n\n";
	cin1 >> ch_num;
	for (int i = 0; i < ch_num; ++i) {
		string ch; double pos;
		cin1 >> ch >> pos;
		cout << ch << " " << pos << "\n";
		ch_pos[ch] = pos;
		pos_ch[pos] = ch;
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
		// Add root
		ch_notes.push_back(c_major_step[i]);
		// Add third
		ch_notes.push_back(c_major_step[(i+2) % L2]);
		// Add fifth
		ch_notes.push_back(c_major_step[(i+4) % L2]);
		for (int j = 0; j < ch_notes.size(); ++j)
			cout << ch_notes[j] << " ";
		cout << "\n";
		chord_notes[c_major_ch[i]] = ch_notes;
	}
}

int main() {
	read_input();
	create_chords();
	// Test double mod
	// cout << double_mod(7.75, L1) << "\n";

	return 0;
}