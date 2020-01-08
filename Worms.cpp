#include<bits/stdc++.h>
using namespace std;

int main(){
    long n = 0;
    cin>>n;
    long arr[n];
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    
    long dp[n+1];
    dp[0] = arr[0];
    for(int i = 1; i < n; i++){
        dp[i] = dp[i-1] + arr[i];
    }
    
    long q = 0;
    cin>>q;
    
    while(q > 0){
        long x = 0;
        cin>>x;
        long lb=0,ub=n-1,mid=0;
        int flag = 0;
        while(lb < ub){
            mid = lb + (ub - lb)/2;
            if(dp[mid] == x){
                cout<<mid+1;
                flag = 1;
                break;
            }else if(x < dp[mid]){
                if(mid-1 >= 0){
                    if(x > dp[mid - 1]){
                        cout<<mid+1;
                        flag = 1;
                        break;
                    }else{
                        ub = mid - 1;
                    }
                }else{
                    cout<<1;
                    flag = 1;
                    break;
                }
            }else{
                if(mid + 1 < n){
                    if(x < dp[mid + 1]){
                        cout<<mid+2;
                        flag = 1;
                        break;
                    }else{
                        lb = mid + 1;
                    }
                }else{
                    cout<<mid+1;
                    flag = 1;
                    break;
                }
            }
        }
        if(flag == 0){
            cout<<ub+1;
        }
        cout<<endl;
        q--;
    }
    return 0;
}
