#define MaxVertexNum 100

typedef char VertexType;
typedef int EdgeType;
typedef struct Mgraph
{
    /* data */
    VertexType vexs[MaxVertexNum];
    EdgeType edges[MaxVertexNum][MaxVertexNum];
    int n, e;
};

void CreateMGraph(Mgraph *G)