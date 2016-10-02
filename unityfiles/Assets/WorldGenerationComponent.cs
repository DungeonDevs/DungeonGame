using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class WorldGenerationComponent : MonoBehaviour
{

    public GameObject Wall;
    public GameObject Ground;
    // Use this for initialization
    void Start()
    {
        int[][] array2D = new int[5][] { new int[10],new int[10],new int[10],new int[10], new int[10] };
        array2D[1][5] = 1;
        array2D[1][6] = 1;
        array2D[1][7] = 1;
        array2D[1][8] = 1;
        array2D[3][5] = 1;
        array2D[3][6] = 1;
        array2D[3][7] = 1;
        array2D[3][8] = 1;
        generateTiles(array2D);
    }
    public void updateMap(string map) {
        Debug.Log(map);
    }
    public void generateTiles(int[][] list)
    {
        int xCo = 0;
        int yCo = 0;
        foreach (int[] x in list)
        {
            foreach (int y in x)
            {
                Debug.Log(y);
                Instantiate(getTile(y), new Vector3(xCo, 0, yCo), Quaternion.identity);
                yCo = yCo + 1;
            }
            yCo = 0;
            xCo = xCo + 1;
        }
    }
    public void generateOverlay(int[][] list)
    {
        int xCo = 0;
        int yCo = 0;
        foreach (int[] x in list)
        {
            foreach (int y in x)
            {
                Debug.Log(y);
                Instantiate(getOverlay(y), new Vector3(xCo, 1, yCo), Quaternion.identity);
                yCo = yCo + 1;
            }
            yCo = 0;
            xCo = xCo + 1;
        }
    }
    public GameObject getTile(int type)
    {
        switch (type)
        {
            case 0:
                return Ground;
            case 1:
                return Wall;
        }
        return null;
    }
    public GameObject getOverlay(int type)
    {
        return null;
    }
    // Update is called once per frame
    void Update()
    {

    }

}
