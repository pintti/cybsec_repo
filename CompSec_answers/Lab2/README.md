# Lab 2: Networks and web security

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