using Assets.Scripts.Brain;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using static UnityEngine.GraphicsBuffer;

public class PacmanBrain : MonoBehaviour
{
    public Pacman pacman;

    public Transform pacmanPos;

    public Transform pelletParent;
    public List<Transform> pelletsPos;

    Transform targetPos;

    public List<Transform> ghostPos;

    public IPacmanLogic pacmanLogic;
    public BFSLogic BFSLogic;
    public DFSLogic DFSLogic;
    public AStarLogic AStarLogic;

    public string actualLogic;

    public PacmanMap pacmanMap;

    public string prevCellId;
    public string currentCellId;

    List<string> directions = new List<string>();
    Vector2 direction = Vector2.right;


    public bool isPowerful;
    public bool saveYourself;

    public void Awake()
    {
        switch (actualLogic)
        {
            case "BFS":
                pacmanLogic = BFSLogic;
                break;
            case "DFS":
                pacmanLogic = DFSLogic;
                break;
            case "AStar":
                pacmanLogic = AStarLogic;
                break;
        }
    }

    private void Start()
    {
        for (int i = 0; i < pelletParent.childCount; i++)
        {
            if (pelletParent.GetChild(i).gameObject.activeSelf)
                pelletsPos.Add(pelletParent.GetChild(i).GetComponent<Transform>());
        }

        pacmanLogic = BFSLogic;
        prevCellId = pacmanMap.objCoordsToIndex(pacmanPos);
    }

    public void FixedUpdate()
    {

        currentCellId = pacmanMap.objCoordsToIndex(pacmanPos);
        if (prevCellId != currentCellId)
        {
            prevCellId = currentCellId;
            if (!isPowerful)
            {
                bool nowSaveYourself = isSaveYourself();
                if (saveYourself == false && nowSaveYourself == true)
                {
                    directions.Clear();
                }
                saveYourself = nowSaveYourself;
            }
            else
            {
                saveYourself = false;
            }

            if (directions.Count == 0)
            {
                ResetTargets();

                targetPos = findTarget(pelletsPos, saveYourself);

                directions = pacmanLogic.FindWay(targetPos, pacmanPos);

                string log = "";
                foreach (string d in directions)
                {
                    log += d + " ";
                }

                Debug.Log("==========PATH " + log);
            }

            string nextDirection = directions.Last();
            Vector2 moveDir = converStrToVector(nextDirection);
            pacman.movement.SetDirection(moveDir);
            direction = moveDir;
            directions.RemoveAt(directions.Count - 1);
            Debug.Log("TURNED " + nextDirection);
        }

    }

    void ResetTargets()
    {
        pelletsPos.Clear();
        for (int i = 0; i < pelletParent.childCount; i++)
        {
            if (pelletParent.GetChild(i).gameObject.activeSelf)
                pelletsPos.Add(pelletParent.GetChild(i).GetComponent<Transform>());
        }
    }

    Transform findTarget(List<Transform> targets, bool isPanic)
    {
        float dist;
        if (!isPanic) dist = float.MaxValue;
        else dist = float.MinValue;
        Transform rez = null;
        foreach (Transform target in targets)
        {
            if (!isPanic)
            {
                if (Vector2.Distance(pacmanPos.position, target.position) < dist)
                {

                    dist = Vector2.Distance(pacmanPos.position, target.position);
                    rez = target;

                }
            }
            else
            {
                float dist1, dist2, dist3, dist4, xDist;
                //DISTANCE TO GHOSTS AND SUM
                dist1 = Vector2.Distance(ghostPos[0].position, target.position);
                dist2 = Vector2.Distance(ghostPos[1].position, target.position);
                dist3 = Vector2.Distance(ghostPos[2].position, target.position);
                dist4 = Vector2.Distance(ghostPos[3].position, target.position);
                xDist = dist1 + dist2 + dist3 + dist4;
                if (xDist > dist)
                {

                    dist = xDist;
                    rez = target;

                }
            }
        }
        return rez;


    }

    bool isSaveYourself()
    {
        foreach (Transform ghost in ghostPos)
        {
            if (Vector2.Distance(pacmanPos.position, ghost.position) < 8.0f)
            {
                return true;
            }
        }
        return false;
    }


    Vector2 converStrToVector(string direction)
    {
        switch (direction)
        {
            case "Up": return Vector2.up;
            case "Down": return Vector2.down;
            case "Right": return Vector2.right;
            case "Left": return Vector2.left;
            default: return Vector2.zero;
        }
    }

    public void OnDeath()
    {
        directions.Clear();
        enabled = false;
    }

}
