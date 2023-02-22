#include "bits.h"
using namespace std;

#define format1 regex("[0-9]{4}\\-[0-9]{2}\\-[0-9]{2}") // YYYY-MM-DD
#define format2 regex("[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}") // DD.MM.YYYY
#define format3 regex("[0-9]{2}\\/[0-9]{2}\\/[0-9]{4}") // MM/DD/YYYY

regex formats[] = {format1, format2, format3};

vector <string> date_by_format(string str, int format){
  vector <string> date;
  if (format == 1) {
    date.push_back(str.substr(0, 4));
    date.push_back(str.substr(str.find("-") + 1, 2));
    date.push_back(str.substr(str.find_last_of("-") + 1, 2));
  }
  if (format == 2) {
    date.push_back(str.substr(str.find_last_of(".") + 1, 4));
    date.push_back(str.substr(str.find(".") + 1, 2));
    date.push_back(str.substr(0, 2));
  }
  if (format == 3) {
    date.push_back(str.substr(str.find_last_of("/") + 1, 4));
    date.push_back(str.substr(0, 2));
    date.push_back(str.substr(str.find("/") + 1, 2));
  }
  return date;
}

class DateCorrector2023 {
    public:
    
    string fix(string token){
      int year, month, day, format;
      format = 0;
      for (int i = 0; i < 3; ++i) if (regex_match(token, formats[i])) format = i + 1;
      if (format == 0) return token;
      vector <string> date = date_by_format(token, format);
      year = stoi(date[0]);
      month = stoi(date[1]);
      day = stoi(date[2]);

      if (year == 2022 && month > 0 && month <= 12 && day > 0 && day <= 31) {
        if (month == 2 && day > 28) return token;
        if (month % 2 == 0 && day > 30) return token;
        return regex_replace(token, regex("2022"), "2023");
      }
      else return token;
    }
};

// YYYY-MM-DD
// DD.MM.YYYY
// MM/DD/YYYY

int main(){
  DateCorrector2023 test;
  cout << test.fix("2022-12-24") << endl;
  cout << test.fix("24.12.2022") << endl;
  cout << test.fix("12/24/2022") << endl;
  return 0;
}