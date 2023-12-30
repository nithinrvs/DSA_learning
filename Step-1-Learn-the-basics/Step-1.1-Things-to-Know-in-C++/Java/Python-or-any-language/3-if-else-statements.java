/*
Problem statement: 
Programming languages have some conditional / decision-making statements that execute when some specific condition is fulfilled.
If-else is one of the ways to implement them.
You are given two numbers 'a' and 'b'.
Compare the numbers and print the relation.
Print “smaller”, “greater” or “equal” when ‘a’ is smaller than ‘b’, greater than ‘b’, or equal to ‘b’ respectively.

Example :
Input: ‘a’ = 5 and ‘b’ = 3
Output: greater
Explanation: Since ‘a’ (= 5) is greater than ‘b’ (= 3), we are printing “greater”.
*/

import java.util.Scanner;

public class Solution {
    public static String compareIfElse(int a, int b) {
        String sol;
        if(a > b){
            sol = "greater";
        }else if(a < b){
            sol = "smaller";
        }else{
            sol= "equal";
        }
        return sol;
    }
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        String inputLine = scanner.nextLine();
        Scanner lineScanner = new Scanner(inputLine);
        int num1 = lineScanner.nextInt();
        int num2 = lineScanner.nextInt();
        String ans = compareIfElse(num1, num2);
        System.out.println(ans);
    }
}