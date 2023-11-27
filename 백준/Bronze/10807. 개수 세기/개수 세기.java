import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] ary = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) ary[i] = Integer.parseInt(st.nextToken());
        int f_n = Integer.parseInt(br.readLine());
        int s = 0;
        for (int i = 0; i < n; i++){
            if (ary[i] == f_n) s += 1;
        }
        System.out.println(s);
        br.close();
    }
}