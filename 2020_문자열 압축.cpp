#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string s) {
	int answer = 0;

	for (int i = 1; i <= s.length(); i++)
	{
		vector<pair<int, string>> v;
		for (int j = 0; j < s.length(); j += i)
		{
			string temp = s.substr(j, i);
			if (v.empty() || v.back().second != temp)
				v.push_back({ 1,temp });
			else if (v.back().second == temp)
				v.back().first++;
		}
		string len = "";
		for (int j = 0; j < v.size(); j++)
		{
			if (v[j].first != 1)
				len += to_string(v[j].first);
			len += v[j].second;
		}
		if (answer == 0 || answer > len.length())
			answer = len.length();
	}
	return answer;
}
int main()
{
	cout << solution("xababcdcdababcdcd");

	return 0;
}