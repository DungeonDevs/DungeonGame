using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;
public class WorldGenerationComponent : MonoBehaviour
{

    public ObjectLoader oL;
    public int playerRotation;
    public int[][] tileMap;
    public int[][] overlay;
    public int[][] sa;
    public GameObject tileParent;
    public GameObject overlayParent;
    public GameObject cam;
    // Update is called once per frame
    void Update()
    {

    }
    // Use this for initialization
    void Start()
    {
        tileParent = GameObject.Find("tileParent");
        overlayParent = GameObject.Find("overlayParent");
        oL = this.GetComponent<ObjectLoader>();
        cam = Camera.main.gameObject;
        /*
        tileMap = new int[5][] { new int[10], new int[10], new int[10], new int[10], new int[10] };
        tileMap[1][5] = 1;
        tileMap[1][6] = 1;
        tileMap[1][7] = 1;
        tileMap[1][8] = 1;
        tileMap[3][5] = 1;
        tileMap[3][6] = 1;
        tileMap[3][7] = 1;
        tileMap[3][8] = 1;
        generateTiles(tileMap);
        overlay = new int[5][] { new int[10], new int[10], new int[10], new int[10], new int[10] };
        overlay[2][6] = 1;
        generateOverlay(overlay);
        */
    }
    public void render(informationClass data)
    {
        cleanOverlay();
        cleanTiles();
        playerRotation = data.playerRoatation;
        generateTiles(data.tiles);
        generateOverlay(data.overlay);
    }
    public void generateTiles(int[][] list)
    {
        int xCo = 0;
        int zCo = 0;
        foreach (int[] x in list)
        {
            foreach (int z in x)
            {
                Debug.Log(xCo +" "+ zCo +":" + z);
                GameObject go = Instantiate(getTile(z), new Vector3(xCo, 0, zCo), Quaternion.identity) as GameObject;
                go.transform.parent = tileParent.transform;
                zCo = zCo + 1;
            }
            zCo = 0;
            xCo = xCo + 1;
        }
    }
    public void generateOverlay(int[][] list)
    {
        int xCo = 0;
        int zCo = 0;
        foreach (int[] x in list)
        {
            foreach (int z in x)
            {
                if (z != 0)
                {
                    GameObject go = Instantiate(getOverlay(z), new Vector3(xCo, 1, zCo), Quaternion.identity) as GameObject;
                    go.transform.parent = overlayParent.transform;
                    if (go.GetComponent<playerComponent>() != null)
                    {
                        go.GetComponent<playerComponent>().__init__(playerRotation);
                    }
                }
                zCo = zCo + 1;
            }
            zCo = 0;
            xCo = xCo + 1;
        }
    }
    public GameObject getTile(int type)
    {
        switch (type)
        {
            case 0:
                return oL.ground;
            case 1:
                return oL.wall;
        }
        return null;
    }
    public GameObject getOverlay(int type)
    {
        switch (type)
        {
            case 1:
                return oL.player;
        }
        return null;

    }
    public void cleanOverlay()
    {
        Camera.main.GetComponent<cameraComponent>().restore();
        foreach (Transform child in overlayParent.transform)
        {
            Destroy(child.gameObject);
        }
    }
    public void cleanTiles()
    {
        foreach (Transform child in tileParent.transform)
        {
            Destroy(child.gameObject);
        }
    }
}
