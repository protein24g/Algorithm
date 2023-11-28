import java.io.*;
import java.util.*;

public class Main{
    public static int n, m;
    public static char[][] ary;
    public static int[] tmp;
    public static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ary = new char[n][];

        for (int i = 0; i < n; i++) ary[i] = br.readLine().toCharArray();
        bfs();

    }
    public static void bfs(){
        Deque<int[]> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        dq.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        while(!dq.isEmpty()){
            int[] xy = dq.poll();
            if(xy[0] == n-1 && xy[1] == m-1){
                System.out.println(xy[2]);
                return;
            }else{
                for(int i = 0; i < 4; i++){
                    int nx = xy[0] + d[i][0], ny = xy[1] + d[i][1];
                    if(0 <= nx && nx < n && 0 <= ny && ny < m){
                        if(!visited[nx][ny] && ary[nx][ny] == '1'){
                            visited[nx][ny] = true;
                            dq.add(new int[]{nx, ny, xy[2]+1});
                        }
                    }
                }
            }
        }
    }
}