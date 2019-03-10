#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

#define NUM_SLIDES 100000
#define NUM_TAGS 505

//ifstream fin ("./input/a_example.txt");
ifstream fin ("./input/e_shiny_selfies.txt");
ofstream fout ("test.out");

int N;
string s;
map <string, int> tag_id;
vector <int> tags[NUM_SLIDES];
vector <int> htype;
int num_tags_total;
int matrix[NUM_TAGS][NUM_TAGS];
vector <int> photos[NUM_TAGS][NUM_TAGS];
vector <int> tag_photo[NUM_TAGS];
vector <int> all_photos;
bool used[NUM_SLIDES];



int main()
{
	cout << "test\n";

	//fin >> s;
	//cout << s << "\n";
	fin >> N;
	cout << N << "\n";
	num_tags_total = 0;
	memset(used, 0, sizeof(used));

	for (int i = 1; i <= N; ++i)
	{
		string pos, c_tag;
		fin >> pos;
		bool c_htype;
		if (pos[0] == 'H') c_htype = true;
		else c_htype = false;
		htype.push_back(c_htype);
		int num_tags;
		fin >> num_tags;
		//cout << num_tags << "\n";
		for (int j = 0; j < num_tags; ++j)
		{
			fin >> c_tag;
			map <string,int>::iterator it = tag_id.find(c_tag);
			if (it != tag_id.end())
			{
				//cout << c_tag << " exists\n";
			}
			else
			{
				num_tags_total++;
				//cout << num_tags_total << "\n";
				//cout << c_tag << " insert\n";
				tag_id[c_tag] = num_tags_total;
			}
			tags[i].push_back(tag_id[c_tag]);
		}
	}
	cout << num_tags_total << "\n";

	// for (int i = 1; i <= N; ++i)
	// {
	// 	cout << i << ": ";
	// 	for (int j = 0; j < tags[i].size(); ++j)
	// 		cout << tags[i][j] << " ";
	// 	cout << "\n";
	// }

	for (int i = 1; i <= N; ++i)
	{
		for (int j = 0; j < tags[i].size(); ++j)
			for (int k = j + 1; k < tags[i].size(); ++k)
			{
				int tag_1 = min(tags[i][j], tags[i][k]);
				int tag_2 = max(tags[i][j], tags[i][k]);
				matrix[tag_1][tag_2]++;
				photos[tag_1][tag_2].push_back(i);
			}

		for (int j = 0; j < tags[i].size(); ++j)
		{
			int tag = tags[i][j];
			tag_photo[tag].push_back(i);
		}
	}

	int NT = num_tags_total;

	// for (int i = 1; i <= NT; ++i)
	// {
	// 	for (int j = 1; j <= NT; ++j)
	// 		cout << matrix[i][j] << " ";
	// 	cout << "\n";
	// }

	for (int i = 1; i <= NT; ++i)
		for (int j = 1; j <= NT; ++j)
			random_shuffle(photos[i][j].begin(), photos[i][j].end());	

	for (int i = 1; i <= NT; ++i)
		random_shuffle(tag_photo[i].begin(), tag_photo[i].end());

	for (int i = 1; i <= N; ++i)
		all_photos.push_back(i);
	random_shuffle(all_photos.begin(), all_photos.end());

	vector <int> ordered_photos;
	bool is_continued = false;
	int T = 0;
	while(all_photos.size() > 0 && T < 200000)
	{
		++T;

		int photo;
		if (!is_continued)
		{
			photo = all_photos.back();
			all_photos.pop_back();
			if (used[photo]) continue;
			ordered_photos.push_back(photo);
			used[photo] = true;
		}
		else
		{
			photo = ordered_photos.back();
		}

		// choose <tag1, tag2>
		// sample from B <tag1, tag2>

		bool success = false;
		int tag_1, tag_2, new_photo;
		for (int j = 0; j < tags[photo].size(); ++j)
		{
			if (success) break;
			for (int k = j + 1; k < tags[photo].size(); ++k)
			{
				tag_1 = min(tags[photo][j], tags[photo][k]);
				tag_2 = max(tags[photo][j], tags[photo][k]);
				new_photo = photos[tag_1][tag_2].back();
				if (new_photo != photo && !used[new_photo])
				{
					success = true;
					break;
				}
				else photos[tag_1][tag_2].pop_back(); 
			}
		}
		if (!success) 
		{
			is_continued = false;
			continue;
		}

		// mark
		ordered_photos.push_back(new_photo);
		used[new_photo] = true;

		// choose photo such that not tag1 and not tag2
		// optional
		// success = false;
		// if (all_photos.size() > 10 && rand() % 10 == 0)
		// {
		// 	int chances = 1;
		// 	while (chances <= 10)
		// 	{
		// 		new_photo = all_photos[all_photos.size() - chances];
		// 		chances++;
		// 		if (used[new_photo]) continue;
		// 		int ok = true;
		// 		for (int i = 0; i < tag_photo[tag_1].size(); ++i)
		// 			if (tag_photo[tag_1][i] == new_photo)
		// 			{
		// 				ok = false;
		// 				break;
		// 			}
		// 		if (!ok) continue;
		// 		for (int i = 0; i < tag_photo[tag_2].size(); ++i)
		// 			if (tag_photo[tag_2][i] == new_photo)
		// 			{
		// 				ok = false;
		// 				break;
		// 			}
		// 		if (!ok) continue;
		// 		success = true;
		// 		ordered_photos.push_back(new_photo);
		// 		used[new_photo] = true;
		// 		break;
		// 	}
		// }
		// if (!success) continue;
		is_continued = true;

		// choose <tag1, tag2>
	}

	if (ordered_photos.size() % 2) ordered_photos.pop_back();

	fout << ordered_photos.size()/2 << "\n";

	for (int i = 0; i < ordered_photos.size(); i += 2)
		fout << ordered_photos[i]-1 << " " << ordered_photos[i+1]-1 << "\n";

	return 0;
}