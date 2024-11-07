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
        s.add(n+1);
        s.add(-1);
        for(int j = 0 ; j < m; j++){ // what? /
            int del_num = sc.nextInt();
            s.add(del_num);
            // compoare
            int mid = 0;
            int tmp1 = del_num - s.lower(del_num) - 1;
            int tmp2 = s.higher(del_num) - del_num - 1 ;
            mid = Math.max(tmp1, tmp2);
            // 
            Integer left = s.lower(del_num);
            if (left != null)
            {
                int tmp3 = 0;
                int tmp4 = 0;
                Integer sibal = s.lower(left);
                if(sibal != null) tmp3 = left - sibal - 1;
                
                // higher of left is del num
                tmp4 = del_num - left - 1 ;
                left = Math.max(tmp3, tmp4);
            }
            else left = 0;

            Integer right = s.higher(del_num);
            if(right !=null)
            {
                int tmp5 = 0;
                int tmp6 = 0;
                tmp5 = right - del_num - 1;
                Integer sibal2 = s.higher(right);
                if (sibal2 != null) tmp6 = sibal2 - right - 1 ;
                right = Math.max(tmp5, tmp6);
            }
            else right = 0;
            // T[i] = max lcl when the del_num is i, and look both side.
            // 0 1 2 3 4 5 6 7 8 9 10 // 11
            // 0 1 2   4 5 6 7 8 9 10 // 3 T[3] = 7
            // 0 1 2   4 5   7 8 9 10 // 3 T[3] = 3 T[6] = 4 // what the fuc is differ from bruteforce.
            // there are only 2 arrays which is affected by new del_num. lower and higher.
            //   1 2   4 5.  7 8 9 10??????????????????
            //  -1 3 6 9
            // why the fuck should we use treeset than?
            // -1 3 9
            // -1 3 6 9
            // -1 2  3 6 9
            // array manage?
            // peices = curr_m + 1
            // 
            // we are missing unchanged area lcn.
            // 
            int ans = Math.max(mid, left);
            ans = Math.max(ans, right);
            System.out.println(ans);
        }

    }
}