import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] ary = new int[n];

        int m = Integer.parseInt(st.nextToken());
        int tmp;

        for (int i = 0; i < n; i++){
            ary[i] = i+1;
        }

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tmp = ary[a-1];
            ary[a-1] = ary[b-1];
            ary[b-1] = tmp;
        }

        for (int i = 0; i < n; i++){
            bw.write(ary[i]+" ");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}