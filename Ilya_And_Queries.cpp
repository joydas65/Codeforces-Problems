#include<bits/stdc++.h>
#include<string>
using namespace std;

int main(){
    string str;
    getline(cin, str);
    int n = str.size();
    long dp[n];
    dp[0] = 0;
    for(int i = 1; i < n; i++){
        if(str[i] == str[i-1])
        dp[i] = dp[i-1] + 1;
        else
        dp[i] = dp[i-1];
    }
    int m = 0;
    cin>>m;
    while(m-- > 0){
        int lb=0,ub=0;
        cin>>lb>>ub;
        if(lb+1 == ub){
            if(str[lb-1] == str[ub-1])
            cout<<1;
            else
            cout<<0;
        }else{
            cout<<dp[ub-1]-dp[lb-1];
        }
        cout<<endl;
    }
    return 0;
}
