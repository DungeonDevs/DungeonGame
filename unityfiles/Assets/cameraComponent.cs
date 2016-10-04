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
        transform.parent = playerComp.transform;
        transform.LookAt(playerComp.transform);
        transform.localPosition = new Vector3(0, offsetY, offsetZ);
    }
    public void restore() {
		transform.parent = null;
        playerGameobject = null;
        playerGameobject = null;
	}
}
