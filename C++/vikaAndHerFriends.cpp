#include <iostream>
using namespace std;
void solve() {
 int n, x, y;
     scanf("%*d %*d %d %d %d", &n, &x, &y);
      bool flag = true;
     while (n--) {
         int a, b;
         scanf("%d %d", &a, &b);
         if ((x + y & 1) == (a + b & 1)) flag = false;
     }
     printf("%s\n", flag ? "YES" : "NO");
 }
 
int main() {
     int t;
     scanf("%d", &t);
    while (t--) {
         solve();
     }
     
     return 0;
}
