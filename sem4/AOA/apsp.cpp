#include<iostream>
using namespace std;

#define V 4
#define INF 99999

void print(int dist[][V]){
    // for(int i=0;i<V;i++){
    //     for(int j=0;j<V;j++){
    //         if (dist[i][j] == INF)
    //             printf("%7s", "INF");
    //         else
    //             printf("%7d", dist[i][j]);
    //     }
    //     cout<<endl;
    // }
    printf("The following matrix shows the shortest distances"
           " between every pair of vertices \n");
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (dist[i][j] == INF)
                printf("%7s", "INF");
            else
                printf("%7d", dist[i][j]);
        }
        printf("\n");
    }
}



void floydWarshall(int graph[][V]){

    int dist[V][V];
    for(int i=0;i<V;i++){
        for(int j=0;j<V;j++){
            dist[i][j]=graph[i][j];
        }
    }
    for(int k=0;k<V;k++){
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j]= dist[i][k]+ dist[k][j];
            }
        }
    }
    print(dist);
}


int main(){

    int graph[V][V] = { {0, 3, INF, 7},
                        {INF, 0, 2, INF},
                        {5, INF, 0, 1},
                        {2, INF, INF, 0}};
    floydWarshall(graph);

    return 0;
}