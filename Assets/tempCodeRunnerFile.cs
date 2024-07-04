// using System;
// using System.Net.Sockets;
// using System.Text; // Add this directive
// using System.Threading;
// using UnityEngine;
// using UnityEngine.XR.Interaction.Toolkit;

// public class TCPTestClient : MonoBehaviour
// {
//     public String Server_Address = "127.0.0.1";
//     public int DataPort = 8052;
//     public int ImagePort = 8053;

//     string serverMessage;
//     public GameObject renderImage;
//     byte[] bytes_image;
//     private bool serverComm = false;

//     private TcpClient socketConnectionData;
//     private TcpClient socketConnectionImage;
//     private Thread clientReceiveThread;
    

//     void Start()
//     {
//         Debug.Log("Unity started");
//         ConnectImageServer();
//     }

//     void Update()
//     {   

//         setImageAsTexture();
//     }

//     private void ConnectDataServer()
//     {
//         try
//         {
//             socketConnectionData = new TcpClient(Server_Address, DataPort);
//             Debug.Log("Data Server Connected");
//         }
//         catch (Exception e)
//         {
//             serverComm = false;
//             Debug.Log("On client connect exception (Data) " + e);
//         }
//     }

//     private void ConnectImageServer()
//     {
//         try
//         {
//             socketConnectionImage = new TcpClient(Server_Address, ImagePort);
//             clientReceiveThread = new Thread(new ThreadStart(ListenForData));
//             clientReceiveThread.IsBackground = true;
//             clientReceiveThread.Start();
//             serverComm = true;
//             Debug.Log("Image Server Connected");
//         }
//         catch (Exception e)
//         {
//             serverComm = false;
//             Debug.Log("On client connect exception (Image) " + e);
//         }
//     }

//     private void setImageAsTexture()
//     {
//         if (serverMessage != null && serverComm == true)
//         {
//             Debug.Log("Got something from Python");
//             Texture2D tex = new Texture2D(100, 100, TextureFormat.BGRA32, true, false);
//             tex.hideFlags = HideFlags.HideAndDontSave;
//             tex.filterMode = FilterMode.Point;
//             tex.LoadImage(bytes_image);
//             renderImage.GetComponent<Renderer>().material.mainTexture = tex;
//         }
//     }

//     public static byte[] DecodeUrlBase64(string s)
//     {
//         Debug.Log(s);
//         s = s.Replace('-', '+').Replace('_', '/').PadRight(4 * ((s.Length + 3) / 4), '=');
        
//         return Convert.FromBase64String(s);
//     }

//     private void ListenForData()
//     {
//         try
//         {
//             Byte[] bytes = new Byte[12400];
//             while (true)
//             {
//                 using (NetworkStream stream = socketConnectionImage.GetStream())
//                 {
//                     int length;
//                     while ((length = stream.Read(bytes, 0, bytes.Length)) != 0)
//                     {
//                         var incomingData = new byte[length];
//                         Array.Copy(bytes, 0, incomingData, 0, length);
//                         serverMessage = Encoding.ASCII.GetString(incomingData); // Encoding is in System.Text
//                         bytes_image = DecodeUrlBase64(serverMessage);
//                         Debug.Log("Received data from server");
//                         Debug.Log(bytes_image);
//                     }
//                 }
//             }
//         }
//         catch (SocketException socketException)
//         {
//             Debug.Log("Socket exception: " + socketException);
//         }
//     }
// }
