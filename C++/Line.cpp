#include <iostream>
#include <vector>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int te = 0; te < t; te++)
    {
        long long n;
        cin>>n;
        string s;
        cin>>s;
        if(n ==1){
            cout<<0<<"\n";
            continue;
        } 
        vector<long long> v;
        long long sum=0;
        for(long long i =0;i<n;++i){
            if(s[i]=='L'){
                sum += i;
            }
            else{
                sum += n-i-1;
            }
        }
        long long idx = 0;
        for(long long j = 0;j<n/2;++j){
            if(s[j] == 'L'){
                s[j] = 'R';
                sum -=j;
                sum +=n-j-1;
                cout<<sum<<" ";
                idx+=1;
            }
            if(s[n-j-1] == 'R'){
                s[n-j-1] ='L';
                sum -= j;
                sum += n-j-1;
                cout<<sum<<" ";
                idx+=1;
            }
        } 
        for(long long i = idx;i<n;++i){
            cout<<sum<<" ";
        }
        cout<<"\n";
    }
    return 0;
}