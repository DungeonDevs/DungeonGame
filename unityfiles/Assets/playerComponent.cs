using UnityEngine;
using System.Collections;

public class playerComponent : MonoBehaviour {
    public int roatation;
    public void __init__(int roatation) {
        transform.Rotate(new Vector3(0,90*roatation,0));
        Camera.main.GetComponent<cameraComponent>().playerGameobject = this.gameObject;
    }
}
