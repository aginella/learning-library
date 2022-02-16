# How do you create a managed SSH session?

1. Open the navigation menu and click Identity & Security. Click Bastion

2.  Under List Scope, in the Compartment list, click the name of the compartment where you want to create a bastion session.

3. Click the name of the session

![Image alt text](images/bastion.png)

4. Click "Create Session" 

![Image alt text](images/create_session.png)

5. Choose a session type by selecting "Managed SSH Session" 

6. Enter a display name for the new session 

![Image alt text](images/managed.png)


7. Under Add SSH Key, provide the public key file of the SSH key pair that you want to use for the session.
Later, when you connect to the session, you must provide the private key of the same SSH key pair.

8. When you are finished, click "Create session"

![Image alt text](images/create_session2.png)



## Acknowledgements
* **Author** - Thea Lazarova, Solution Engineer Santa Monica
* **Contributors** - Andrew Hong, Solution Engineer Santa Monica

