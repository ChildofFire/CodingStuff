#https://www.hackerrank.com/challenges/short-palindrome/problem
def counttuples(string):
	lookup1=[0]*26
	lookup2=[]
	lookup3=[]
	lookup4=[]

	for i in range(26):
		lookup2.append([0]*26)
	for i in range(26):
		temp=[]
		for j in range(26):
			temp.append([0]*26)
		lookup3.append(temp)
	for i in range(26):
		temp=[]
		for j in range(26):
			temp2=[]
			for k in range(26):
				temp2.append([0]*26)
			temp.append(temp2)
		lookup4.append(temp)
	for i in string:
		c=ord(i)-ord('a')
		for j in range(26):
			lookup4[c][j][j][c]+=lookup3[c][j][j]
			lookup3[j][c][c]+=lookup2[j][c]
			lookup2[j][c]+=lookup1[j]
		lookup1[c]+=1
	answer=0
	for i in range(26):
		for j in range(26):
			answer+=lookup4[i][j][j][i]
	return answer%1000000007

string=input().strip()
print(counttuples(string))

'''
editorial code (Java):
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    static int mod = 1000*1000*1000 + 7;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        int[] arr1 = new int[26];
        int[][] arr2 = new int[26][26];
        int[] arr3 = new int[26];
        int ans = 0;
        for (int i = 0; i < s.length();i++){
            int index = (int)(s.charAt(i)-'a');
            ans += (arr3[index]%mod);
            ans = ans%mod;
            for (int j = 0; j < 26; j++){
                arr3[j] += (arr2[j][index]%mod);
                arr3[j] = arr3[j]%mod;
            }
            for (int j = 0; j < 26;j++){
                arr2[j][index] += (arr1[j]%mod);
                 arr2[j][index] =  arr2[j][index]%mod;
            }
            
            arr1[index]++;
            arr1[index] = arr1[index]%mod;
        }
        System.out.println(ans);
    }
}
'''