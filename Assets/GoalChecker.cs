using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GoalChecker : MonoBehaviour
{
    public Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {
        //rb = GameObject.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other){
        if(rb.velocity.magnitude<0.1){
            rb.velocity = new Vector3(0,0,20);
        }
        GameObject otherGameObject = other.gameObject;
        float alpha = otherGameObject.transform.rotation.y * Mathf.PI/ 180f;
        float beta = Mathf.Atan(rb.velocity.z/rb.velocity.x);

        float answer = Mathf.PI/2 + alpha - beta;

        Vector3 newVelocity = new Vector3(Mathf.Sin(answer), 0, -Mathf.Cos(answer));
        Debug.Log("Hey Sexy");
        rb.velocity = 50 * newVelocity;
    }
}
