using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuEvents : MonoBehaviour
{
    public void BFSPlay()
    {
        SceneManager.LoadScene("PacmanBFS");
    }

    public void DFSPlay()
    {
        SceneManager.LoadScene("PacmanDFS");
    }
    public void AStarPlay()
    {
        SceneManager.LoadScene("PacmanAStar");
    }
    public void ManualPlay()
    {
        SceneManager.LoadScene("PacmanManual");
    }
    public void Exit()
    {
        Application.Quit();
    }

    public void BackToMenu()
    {
        SceneManager.LoadScene("Menu");
    }
}
