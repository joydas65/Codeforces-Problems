#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	int t, sum = 0;
	cin >> t;
	while (t-- > 0) {
		cin >> n;
		int arr[n];
		sum = 0;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
			sum += arr[i];
		}
		if (sum % 2 == 1) {
			cout << "NO" << "\n";
		} else {
			sum = sum / 2;
			bool subset[n + 1][sum + 1];
			
			for (int i = 0; i <= n; i++) {
				subset[i][0] = true;
			}
        		
        	for (int i = 1; i <= sum; i++) {
        		subset[0][i] = false;
        	}
        	
        	for (int i = 1; i <= n; i++) {
        		for (int j = 1; j <= sum; j++) {
            		if (j < arr[i - 1])
                		subset[i][j] = subset[i - 1][j];
            		if (j >= arr[i - 1])
                		subset[i][j] = subset[i - 1][j] || subset[i - 1][j - arr[i - 1]];
        		}
    		}
    		
    		if (subset[n][sum] == true) {
    			cout << "YES" << "\n";
    		} else {
    			cout << "NO" << "\n";
    		}
		}
	}
	return 0;
}
