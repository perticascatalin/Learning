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

double double_mod(double num, int m)
{
	int inum = int(num);
	double rem = num - inum;
	return (inum % m) + rem;
}

int main()
{
	ifstream cin1("ch_pos.in");
	ifstream cin2("c_major_ch.in");

	cin1 >> ch_num;
	for (int i = 0; i < ch_num; ++i)
	{
		string ch; double pos;
		cin1 >> ch >> pos;
		cout << ch << " " << pos << "\n";
		ch_pos[ch] = pos;
		pos_ch[pos] = ch;
	}

	// Test double mod
	// cout << double_mod(7.75, L1) << "\n";

	cin2 >> c_major_num;
	for (int i = 0; i < c_major_num; ++i)
	{
		string step;
		cin2 >> step;
		c_major_step.push_back(step);
	}
	for (int i = 0; i < c_major_num; ++i)
	{
		string chord;
		cin2 >> chord;
		c_major_ch.push_back(chord);
	}

	cout << "Reached this place !!" << "\n";
	for (int i = 0; i < c_major_ch.size(); ++i) cout << c_major_ch[i] << "\n";

	return 0;
}