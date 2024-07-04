using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Collision : MonoBehaviour
{   
    public Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {

        rb.velocity = new Vector3(50f, 0, 2f);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerEnter(Collider other){
        GameObject otherGameObject = other.gameObject;
        float alpha = otherGameObject.transform.rotation.y * Mathf.PI/ 180f;
        float beta = Mathf.Atan(rb.velocity.z/rb.velocity.x);

        float answer = Mathf.PI + alpha - beta;

        Vector3 newVelocity = new Vector3(Mathf.Sin(answer), 0, -Mathf.Cos(answer));

        rb.velocity = 50 * newVelocity;
    }
}
