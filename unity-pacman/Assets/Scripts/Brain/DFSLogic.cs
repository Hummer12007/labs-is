using Assets.Scripts.Brain;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DFSLogic : MonoBehaviour, IPacmanLogic
{

    public PacmanMap graph;

    public List<string> FindWay(Transform target, Transform pacman)
    {
        string start = graph.objCoordsToIndex(pacman);
        string goal = graph.objCoordsToIndex(target);

        HashSet<string> visited = new HashSet<string>();

        Stack<(List<string>, string)> nodes = new Stack<(List<string>, string)>();
        nodes.Push((new List<string>(), start));

        while (nodes.Count > 0)
        {
            (List<string>, string) current = nodes.Pop();
            List<string> path = current.Item1;
            string coords = current.Item2;
            if (current.Item2 == goal)
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
                nodes.Push((tmp, neighbours.GetValueOrDefault("Up")));
            }
            if (neighbours.ContainsKey("Down"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Down");
                nodes.Push((tmp, neighbours.GetValueOrDefault("Down")));
            }
            if (neighbours.ContainsKey("Left"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Left");
                nodes.Push((tmp, neighbours.GetValueOrDefault("Left")));
            }
            if (neighbours.ContainsKey("Right"))
            {
                List<string> tmp = new List<string>(path);
                tmp.Add("Right");
                nodes.Push((tmp, neighbours.GetValueOrDefault("Right")));
            }
        }
        return null;
    }

}
