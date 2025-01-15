#include <iostream>
#include <array>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

class Stack
{

private:
  int arra[100];

  int pointer = -1;

public:
  void push(int x)
  {
    if (pointer == 100)
    {
      cout << "Stack Over Flow";
    }
    else
    {
      arra[++pointer] = x;

      cout << "Pushed " << x << " to Stack" << endl;
    }
  }

  void pop()
  {
    if (pointer == -1)
    {
      cout << "Stack is Empty" << endl;
    }
    else
    {
      cout << arra[pointer--] << " is Popped from stack" << endl;
    }
  }

  void top()
  {
    if (pointer == -1)
    {
      cout << "Stack is Underflow" << endl;
    }
    else
    {
      cout << arra[pointer] << endl;
    }
  }
  int inserttop(int x)
  {
    arra[pointer] = x;
    cout << arra[pointer] << "is inserted" << endl;
  }
  int empty()
  {
    if (pointer == -1)
    {
      cout << "Stack is Underflow." << endl;
    }
    else
    {
      cout << "Stack is not Underflow. Pointer is at " << arra[pointer] << endl;
    }
  }
};
Stack firststack;
string strtolower(string);
int myfunction();
int main()
{
  myfunction();
}
string strtolower(string data)
{

  transform(data.begin(), data.end(), data.begin(), [](unsigned char c)
            { return std::tolower(c); });
  return data;
}
int myfunction()
{

  string funtion;
  int value;
  char ans;
  cout << "Enter your operation to stack :";
  cin >> funtion;
  funtion = strtolower(funtion);
  if (funtion == "push")
  {
    cout << "Enter Value :";
    cin >> value;
    cout << endl;
    firststack.push(value);
  }
  else if (funtion == "top")
  {
    cout << "Do you want to update top value : Y or N";
    cin >> ans;
    ans = tolower(ans);
    if (ans == 'y')
    {
      cout << "Enter Value :";
      cin >> value;
      cout << endl;
      firststack.inserttop(value);
    }
    else
    {
      firststack.top();
    }
  }
  else if (funtion == "pop")
  {
    firststack.pop();
  }
  else if (funtion == "empty")
  {
    firststack.empty();
  }
  else if (funtion == "close")
  {
    cout << "Closed";
    return 0;
  }

  myfunction();
}
