#include "bits.h"

using namespace std;

// https://www.softwaretestinghelp.com/regex-in-cpp/
// regex expr("<expr>")
// regex_match(str, expr) > true / false
// regex_replace(str, expr, word)
// regex_search(str, smatch m, expr)

// str.find("<delimiter>")
// str.find_last_of("<delimiter>")
// str.substr(start, size)
// stoi(str) > int

// Date Corrector 2023
#define format1 regex("[0-9]{4}\\-[0-9]{2}\\-[0-9]{2}") // YYYY-MM-DD
#define format2 regex("[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}") // DD.MM.YYYY
#define format3 regex("[0-9]{2}\\/[0-9]{2}\\/[0-9]{4}") // MM/DD/YYYY

// 2022-MM-DD
string format1_year(string str){
  return str.substr(0, 4);
}

// YYYY-02-DD
string format1_month(string str){
  int start = str.find("-");
  return str.substr(start + 1, 2);
}

// YYYY-MM-22
string format1_day(string str){
  int start = str.find_last_of("-");
  return str.substr(start + 1, 2);
}

// DD.MM.2023
string format2_year(string str){
  int start = str.find_last_of(".");
  return str.substr(start + 1, 4);
}

// DD.03.YYYY
string format2_month(string str){
  int start = str.find(".");
  return str.substr(start + 1, 2);
}

// 30.MM.YYYY
string format2_day(string str){
  return str.substr(0, 2);
}

// MM/DD/2023
string format3_year(string str){
  int start = str.find_last_of("/");
  return str.substr(start + 1, 4);
}

// 04/DD/YYYY
string format3_month(string str){
  return str.substr(0, 2);
}

// MM/31/YYYY
string format3_day(string str){
  int start = str.find("/");
  return str.substr(start + 1, 2);
}

string year_by_format(string str, int format) {
  if (format == 1) return format1_year(str);
  if (format == 2) return format2_year(str);
  if (format == 3) return format3_year(str);
  return "";
}

string month_by_format(string str, int format) {
  if (format == 1) return format1_month(str);
  if (format == 2) return format2_month(str);
  if (format == 3) return format3_month(str);
  return "";
}

string day_by_format(string str, int format) {
  if (format == 1) return format1_day(str);
  if (format == 2) return format2_day(str);
  if (format == 3) return format3_day(str);
  return "";
}

string fix(string token){
  int year, month, day, format;
  format = 0;
  if (regex_match(token, format1)) format = 1;
  if (regex_match(token, format2)) format = 2;
  if (regex_match(token, format3)) format = 3;
  if (format == 0) return token;

  year = stoi(year_by_format(token, format));
  month = stoi(month_by_format(token, format));
  day = stoi(day_by_format(token, format));

  if (year == 2022 && month > 0 && month <= 12 && day > 0 && day <= 31) {
    if (month == 2 && day > 28) return token;
    if (month % 2 == 0 && day > 30) return token;
    return regex_replace(token, regex("2022"), "2023");
  }
  else return token;
}

int main(){

  cout << fix(string("2023-02-22")) << endl;
  cout << fix(string("14.07.1991")) << endl;
  cout << fix(string("14.07.2022")) << endl;
  cout << fix(string("03/01/2022")) << endl;
  cout << fix(string("02/29/2022")) << endl;
  cout << fix(string("2023-02-222")) << endl;
  cout << fix(string("202322.0332.22222")) << endl;

  return 0;
}