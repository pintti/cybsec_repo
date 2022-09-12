# Lab 2: Networks and web security

## Instructions

Below is a copy of the questions found in the Network lab folder. Answer the questions here. In task 3 put the server code and the XSS-script to a different file. Also the picture and the report in task 4 can be returned as a separe files.

Note that there is reserved folder for specific tasks.

## Task 1
## Basic SQL Injections

### Errors

The query used to cause a searh was q='juice'. This caused an syntax error that happened due to the single quotes closing a statement earlier than expected. This gap can be exploited for SQL injection.

```SQL
SELECT * FROM Products WHERE ((name LIKE '%SEARCHRESULT%' OR description LIKE '%SEARCHRESULT%') AND deletedAt IS NULL) ORDER BY name"
```

### Deleted item!

Items are deleted by checking whether or not the deletedAt column is NULL. Getting all the items is as simple as stopping the above command short by commenting out the rest of the query, so that the SQL looks like this.

```SQL
SELECT * FROM Products WHERE ((name LIKE '%'))--SEARCHRESULT%' OR description LIKE '%SEARCHRESULT%') AND deletedAt IS NULL) ORDER BY name"
```

This works due to the SQL query being complete and the rest of the query being a comment that the SQL server ignores.

### Concrete Error

By applying different kinds of SQL injections to the login fields, it is possible to see that the query going to the SQL server in this case is 

```SQL
SELECT * FROM Users WHERE email = 'EMAIL' AND password = 'PASSWORD' AND deletedAt IS NULL
```
This is the SQL command we want to break by injecting. If the email field is injected with the following "' OR 1=1 --", the command morphs into 
```SQL
SELECT * FROM Users WHERE email = '' OR 1=1 --' OR AND password = 'PASSWORD' AND deletedAt IS NULL
```
As can be seen this makes it so that the query returns a user with the email '' or the first user in the table. Obviously no user with '' email exists, so the query returns the first user in the table Users, which happens to be the admin.

Alternatively, it is possible to checkout the reviews on the site and see that the email address of the admin is admin@juice-sh.op. This can be used in a targeted attack by making the email field the following "admin@juice-sh.op'--". Again this makes the query
```SQL
SELECT * FROM Users WHERE email = 'admin@juice-sh.op'--' OR AND password = 'PASSWORD' AND deletedAt IS NULL
```
and this logs us in as the user with the admins email, which happens to be the admin.

## Inspecting the client resources

### Scoreboard

Using the developer tools it is possible to open the main.js of the site. Upon closer inspection of the main.js we can find references to the Scoreboard as "scoreBoard" and "score-board". Trying to access localhost:3000/#/score-board nets us access to the actual score board.

### Administration panel

Doing the same as above, we can find references to "administration". Accessing localhost:3000/#/adminitration while logged in as the admin gives us the administration panel.

## XSS attacks

### Pop-up

DOM based XSS modifies the users environment, without making any changes to the server itself. The HTTP is unchanged, but the users client side changes due to the script. For the reflected attack, the attack bounces back from the server. If a trusted user for example clicks a link that has XSS attack in it, the server trusts the users link and bounces that back to the user as a response where the XSS can then execute.

### Persistent XSS

The server should validate inputs on both client and server-side, and all variables should be sanitized or escaped.

## Task 2 

**'These are not my credentials'**

SQL command
 ```sql
 ')) UNION SELECT id, username, email, password, createdAt, updatedAt, deletedAt, password FROM Users--

```

In SQL the UNION operator combines two or more SELECT statements. Thanks to that, it is possible to inject another SELECT command from a different table within the one before, if the field isn't sanitized. The problem for the attacker comes from not knowing how many columns are required for the information to register, but this can be found out by a select number of methods. If the server accepts the command, UNION modifier combines the two results, even if that includes data from tables where the attacker shouldn't be able to access.


---
**Cross-site request forgery**

*Returns:*
* index.html

---

**Brute forcing**

*Returns:*
* Wordlist
* Any code you created.
* Detailed description on how you created the wordlist and how you did the brute force attack.

---

## Task 3


*Returns:*

* Your own server code or a description of how you showed the received data.
* Your own HTML/Javascript/etc. code **without directory traversal characters in its name**.
* The *zip* archive that you uploaded to overwrite the subtitle file.
* **Clear** instructions on how to start your own server, send the XSS attack and how to verify that the information was sent to your server from Juice Shop.
---

## Task 4

You can complete this task in two ways. You can do the predefined task or you can suggest a task that interests you and do that. __Contact the course assistants__ and describe them what you are interested on doing/trying to do. If they say it is good you can do that as your task 4.

*Return predefined task(s) here or into separate folder. If you chose to implement something own, return them to separate folder.*



























