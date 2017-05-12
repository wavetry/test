#include <iostream>
#include <string>
using namespace std;
int main(){
	string a="hello world";
    string b=a;
    if (a.c_str()==b.c_str())
    {
        cout<<"true"<<endl;
    }
	return 0;
}