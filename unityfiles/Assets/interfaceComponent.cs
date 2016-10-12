using UnityEngine;
using System;
using System.IO;
using Newtonsoft.Json;
public class interfaceComponent : MonoBehaviour
{
    public WorldGenerationComponent worldGen;
    private string old;
    void Start()
    {
        worldGen = GameObject.FindObjectOfType<WorldGenerationComponent>();
        StreamWriter sr = new StreamWriter("../src/engine/unityPy.txt");
        sr.Write("ready");
        sr.Close();
    }
    void Update(){
        try{
            using (StreamReader sr = new StreamReader("../src/engine/pyUnity.json"))
            {
                string content = sr.ReadToEnd();
                if (content == old) return;
                print(content);
                if (content == "close")
                {
                    Application.Quit();
                }
                else if (content == "loading")
                {
                    showLoadingScreen();
                }
                else
                {
                    print("rendering");
                    worldGen.render(JsonConvert.DeserializeObject<informationClass>(content));
                }
                old = content;
            }
        }
        catch (Exception e){Debug.LogError("The file could not be read.");}
    }
    void showLoadingScreen(){}
}