using UnityEngine;
using System.Collections;

public class cameraComponent : MonoBehaviour
{

    public GameObject playerGameobject;
    public playerComponent playerComp;
    public float offsetZ;
    public float offsetY;
    // Use this for initialization
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (playerGameobject == null) return;
        if (playerComp == null) playerComp = playerGameobject.GetComponent<playerComponent>();
        transform.parent.position = playerComp.transform.position;
        transform.parent.rotation = playerComp.transform.rotation;
        transform.LookAt(transform.parent);
        transform.localPosition = new Vector3(0, offsetY, offsetZ);
    }
    public void restore()
    {
        playerComp = null;
        playerGameobject = null;
    }
}
