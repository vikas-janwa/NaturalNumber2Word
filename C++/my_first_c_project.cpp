#include <iostream>
#include <math.h>
#include <array>
#include <string.h>
#include <vector>
using namespace std;
int* get_user_input ();
int main (){
get_user_input();
return 0;
}

int* get_user_input () {
    int numberOfCources;
    double totalMarks = 0;

    cout << "Enter number of Cources you have completed : ";
    cin >> numberOfCources;

    vector<string> nameOfCource(numberOfCources);
    vector<int> numberInCources(numberOfCources);

     for (int i= 0; i < numberOfCources; i++ ){
       cout << "Enter name of " << i+1 << " course : ";
       cin >> nameOfCource[i];
       cout << "Enter marks in " << nameOfCource[i] << " course : ";
       cin >> numberInCources[i];
     }

     for (int j=0; j <numberOfCources; j++ ){
     cout << "Marks in "<< nameOfCource[j] << ": = " << numberInCources[j] << endl;
     totalMarks += numberInCources[j];

     }
     double CGPA = totalMarks/numberOfCources;
     cout << "Your CGPA is: " << CGPA;

}