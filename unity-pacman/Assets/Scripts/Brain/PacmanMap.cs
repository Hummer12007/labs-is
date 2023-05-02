using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PacmanMap : MonoBehaviour
{
    public List<List<int>> map = new List<List<int>>();
    public Dictionary<string, Dictionary<string, string>> graph = new Dictionary<string, Dictionary<string, string>>();
    public float xStart = -13.5f, xEnd = 13.5f, yStart = -16.5f, yEnd = 13.5f;
    public float xOffset = 14.5f, yOffset = 16.5f;
    public LayerMask obstacleLayer;
    private void Awake()
    {
        fieldToMap();
        mapToGraph();
    }

    public string objCoordsToIndex (Transform obj)
    {

        
        int xInd = coordToInd(obj.position.x, xOffset);
        int yInd = coordToInd(obj.position.y, yOffset);
        
        return ""+yInd+" "+xInd;
    }

    public void fieldToMap()
    {
        for (float y = yStart; y <= yEnd; y++)
        {
            List<int> tmp = new List<int>();
            if (y != -0.5) tmp.Add(-1);
            else tmp.Add(0);
            for (float x = xStart; x <= xEnd; x++)
            {
                RaycastHit2D hit = Physics2D.Raycast(new Vector2(x, y), Vector2.down, 0.4f, obstacleLayer);

                if (hit.collider == null) tmp.Add(0);

                else tmp.Add(-1);
            }
            if (y != -0.5) tmp.Add(-1);
            else tmp.Add(0);
            map.Add(tmp);
        }
    }

    void mapToGraph()
    {
        for(int i=0; i<map.Count; i++)
        {
            for(int j=0; j<map[i].Count; j++)
            {
                if (map[i][j] == -1) { continue; }
                if (map[i][j] == 0) {
                    Dictionary<string, string> dirs = new Dictionary<string, string>();
                    //string DIRS = "";
                    if (i!=0&&map[i - 1][j] == 0)
                    {
                        dirs.Add("Down", ""+(i - 1)+" "+j );
                        //DIRS += " Down " + (i - 1) + j;
                    }
                    if(i!=map.Count-1 && map[i + 1][j] == 0)
                    {
                        dirs.Add("Up", ""+(i + 1)+" "+ j );
                        //DIRS += " Up " + (i + 1) + j;
                    }
                    if (j!=0&&map[i][j - 1]==0)
                    {
                        dirs.Add("Left", ""+i+" "+ (j - 1));
                        //DIRS += " Left " + i + (j-1);
                    }
                    if (j != map[i].Count-1 && map[i][j+1] == 0)
                    {
                        dirs.Add("Right",""+ i+ " "+(j + 1 ));
                        //DIRS += " Right " + i + (j+1);
                    }
                    graph.Add(i.ToString()+" "+j.ToString(), dirs);
                    
                    //Debug.Log("ID : "+i+" "+j+" DIRECTIONS : " +DIRS);
                }
            }
        }
        
    }

    public int coordToInd(float coord, float offset)
    {
        return Mathf.RoundToInt(coord + offset);
    }
}
