using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MidPoint : MonoBehaviour
{
    public Transform p1;
    public Transform p2;
    public Transform target;
    public float yVal;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        target.position = new Vector3((p1.position.x + p2.position.x)/2,yVal,(p1.position.z + p2.position.z)/2);
    }
}
