// my first program in C++
#include <iostream>
using namespace std;

int main()
{
  int N;
  cin >> N;

  int cells [N];

  for (int i = 0; i < N; ++i)
  {
    cin >> cells[i];
  }

  for (int i = 0; i < N; ++i)
  {
    int cell;
    cell = 0;

    // count before, unless first
    if (i > 0 && cells[i-1] != 0) { ++cell; }

    // count self
    if (cells[i] != 0) { ++cell; }

    // count after, unless last
    if (i < N - 1 && cells[i+1] != 0) { ++cell; }

    cout << cell;

    return 0;
  }
}
