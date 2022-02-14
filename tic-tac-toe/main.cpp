#include <iostream>
#include <cstring>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;
struct Anketa
	{
		unsigned int id;
		unsigned int score;
		string name;
		unsigned short age;
	};
vector<Anketa> spisok;
int main() {
	string line;
	ifstream in("profiles.dat");
	int j = 0; 
    if (in.is_open())
    {
        while (getline(in, line))
        {
        	int i = 0;
        	spisok.push_back(Anketa());
            vector<string> arr;
			string str = line;
			string delim(" ");
			size_t prev = 0;
			size_t next;
			size_t delta = delim.length();
			while( ( next = str.find( delim, prev ) ) != string::npos ){
				string tmp = str.substr( prev, next-prev );
				// cout << "I: " << i << endl;
				// cout << "TMP :" << tmp << endl;
				//// cout << "STOI TMP" << stoi(tmp) << endl;
				if (i == 0) {spisok[j].id = stoi(tmp);}
				else if (i == 1) {spisok[j].score = stoi(tmp);}
				else if (i == 2) {spisok[j].name = tmp.data();}
				arr.push_back( str.substr( prev, next-prev ) );
				prev = next + delta;
				i++;
			}
			string tmp = str.substr( prev );
			// cout << "TMP (1):" << tmp << endl;
			spisok[j].age = stoi(tmp);
			// cout << "-------" << endl;
			arr.push_back( str.substr( prev ));
			j++;
        }
    } else {
    	cout << "Can't open file!";
    	return -1;
	}
    in.close();
    cout << " ID |SCORE|   NAME   | AGE|"<< endl;
    for (int i = 0; i <= j; i++) {
    	auto s = spisok[i];
    	if (spisok[i].score >= 30){
    		cout << setw(4) << s.id << "|" << setw(5) << s.score << "|" << setw(10) << s.name << "|" << setw(4) << s.age << "|" << endl; 
		}
	}
	return 0;
}	
