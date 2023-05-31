#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

static long findMissing(std::vector<long> list);

int main(){
  std::vector<long> test {1, 3, 5, 9, 11};
  std::vector<long>test2 {-4, -2, 2, 4, 6};
  cout << findMissing({1, 3, 7})<<endl;
  cout << findMissing(test)<<endl;
  cout << findMissing(test2) <<endl;
  return 0;   
}

static long findMissing(std::vector<long> list){
  //Find how many elements are in the array
  long totalSize = long(list.size());
  //Find the difference of the max and min over the size such the difference is common
  long diff = (list[totalSize - 1] - list[0])/totalSize;
  //Start initial variable at first post
  long initial = list[0];
  //Loop over all elements and if something is not there, return that missing element, otherwise keep adding the initial by the difference
  for(long i: list){
   if(initial != i){
    return initial;
   }
   initial += diff;
  }
  return initial;
}