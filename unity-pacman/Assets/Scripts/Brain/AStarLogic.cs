using Assets.Scripts.Brain;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Unity.VisualScripting;
using UnityEngine;
using Util;

public class AStarLogic : MonoBehaviour, IPacmanLogic
{
    public PacmanMap graph;

    int heuristic(string idCell, List<int> idGoal)
    {
        List<string> cellList = idCell.Split(' ').ToList();
        return Math.Abs(Convert.ToInt32(cellList[0]) - idGoal[0]) + Math.Abs(Convert.ToInt32(cellList[1]) - idGoal[1]);
    }

    public List<string> FindWay(Transform target, Transform pacman)
    {
        string start = graph.objCoordsToIndex(pacman);
        string goal = graph.objCoordsToIndex(target);
        List<string> idGoal = goal.Split(' ').ToList();
        List<int> intIdGoal = new List<int>();
        intIdGoal.Add(Convert.ToInt32(idGoal[0]));
        intIdGoal.Add(Convert.ToInt32(idGoal[1]));
        HashSet<string> visited = new HashSet<string>();
        NodeComparer comparer = new NodeComparer();
        PriorityQueue<(List<string>, int, int, string), NodeComparer> nodes = new PriorityQueue<(List<string>, int, int, string), NodeComparer>();
        nodes.Enqueue((new List<string>(), heuristic(start, intIdGoal), 0, start), comparer);

        while (nodes.Count > 0)
        {
            (List<string>, int, int, string) current = nodes.Dequeue();
            List<string> path = current.Item1;
            int heur = current.Item2;
            int cost = current.Item3;
            string coords = current.Item4;
            if (current.Item4 == goal)
            {
                path.Reverse();
                return path;
            }
            if (visited.Contains(coords))
            {
                continue;
            }
            visited.Add(coords);

            Dictionary<string, string> neighbours = graph.graph.GetValueOrDefault(coords);
            if (neighbours.ContainsKey("Up"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Up");
                string c = neighbours.GetValueOrDefault("Up");
                nodes.Enqueue((tmp, cost+heuristic(c, intIdGoal), cost+1, c), comparer);
            }
            if (neighbours.ContainsKey("Down"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Down");
                string c = neighbours.GetValueOrDefault("Down");
                nodes.Enqueue((tmp, cost + heuristic(c, intIdGoal), cost + 1, c), comparer);
            }
            if (neighbours.ContainsKey("Left"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Left");
                string c = neighbours.GetValueOrDefault("Left");
                nodes.Enqueue((tmp, cost + heuristic(c, intIdGoal), cost + 1, c), comparer);
            }
            if (neighbours.ContainsKey("Right"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Right");
                string c = neighbours.GetValueOrDefault("Right");
                nodes.Enqueue((tmp, cost + heuristic(c, intIdGoal), cost + 1, c), comparer);
            }
        }
        return null;
    }

    
}
