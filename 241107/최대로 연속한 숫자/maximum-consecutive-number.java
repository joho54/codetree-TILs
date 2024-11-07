// how can i get longest consequantial numbrs, lcn, by treeset?
// add treeset, orders ascendingily. 
// how about removal?
// length.
// 1. i can call s.higher(curr_i) and compare it and set max legnth.
// 2. don't know..
// O(nm)
// 1 2 3 5
// or put deleted nubmers in another set.
// 4 6 
// then? compare
// smallest = s.first() 
// largest = s.last()
// curr_num = s.first()
// legnth = initiated
// next_num = s.higher(curr_num)
// compare: next_num - curr_num = 4-1, (1, 2, 3)
// while(next_num != largest())

// m= numbers2del
// 1, 2, 3,4 ,5
// del 2
// 1 3 4 5

import java.util.Scanner;
import java.util.TreeSet;

public class Main {

    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Integer> s = new TreeSet<>();
    public static void main(String[] args) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        // jjjjjjjjj, mmmmmm
        s.add(n+1); // for initiation
        for(int j = 0 ; j < m; j++){
            int del_num = sc.nextInt();
            s.add(del_num);
            int largest = n;
            int samllest = -1;
            int curr_num = samllest;// should be up in while
            int next_num = s.higher(curr_num); // should be updated in wihle
            int last_del = s.last();
            int ans = -1;
            for(int ptr: s){
                // ptr is next
                next_num = ptr;
                // compare
                int tmp = next_num - (curr_num+1);
                // what happens here?
                // System.out.println(next_num + " " + curr_num+1);
                // 0 1 2 3 4 5 6 7 8 
                ans = Math.max(ans, tmp);
                // update curr_num
                curr_num = ptr;
            }
            System.out.println(ans);
        }

    }
}