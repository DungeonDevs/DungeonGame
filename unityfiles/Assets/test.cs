using UnityEngine;
using SocketIO;

public class test : MonoBehaviour
{

    public SocketIOComponent socket;
    public WorldGenerationComponent generator;
    // Use this for initialization
    void Start()
    {
        GameObject go = GameObject.Find("SocketIO");
        socket = go.GetComponent<SocketIOComponent>();
		generator = GameObject.Find("GenerateWorld").GetComponent<WorldGenerationComponent>();
        socket.On("updateMap", updateMap);
    }
    public void updateMap(SocketIOEvent e)
    {
        generator.updateMap(string.Format("{0}", e.data));
    }


    // Update is called once per frame
    void Update()
    {

    }
}
