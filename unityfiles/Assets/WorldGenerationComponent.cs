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
    void Start()
    {
        tileParent = GameObject.Find("tileParent");
        overlayParent = GameObject.Find("overlayParent");
        oL = this.GetComponent<ObjectLoader>();
        cam = Camera.main.gameObject;
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
                zCo++;
            }
            zCo = 0;
            xCo++;
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
                        go.GetComponent<playerComponent>().__init__(playerRotation);
                }
                zCo++;
            }
            zCo = 0;
            xCo++;
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
    public void cleanTiles(){
        foreach (Transform child in tileParent.transform)
        {
            Destroy(child.gameObject);
        }
    }
}