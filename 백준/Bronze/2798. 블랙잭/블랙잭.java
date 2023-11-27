import java.io.*;
import java.util.*;

public class Main {
    static int hap = 0, maxx = 0;
    static int n, m;
    static int[] ary;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ary = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) ary[i] = Integer.parseInt(st.nextToken());
        npr(0, 3, new int[3], ary, new boolean[n]);
        System.out.println(maxx);
    }
    public static void npr(int depth, int r, int[] res, int[] ary, boolean[] visited){
        if(depth == r){
            int s = 0;
            for(int i: res) s += i;
            if(m >= s){
                if(maxx <= s) maxx = s;
            }
            return;
        }else{
            for(int i = 0; i < ary.length; i++){
                if(!visited[i]){
                    visited[i] = true;
                    res[depth] = ary[i];
                    npr(depth + 1, r, res, ary, visited);
                    visited[i] = false;
                }
            }
        }
    }
}