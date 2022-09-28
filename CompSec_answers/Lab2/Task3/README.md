# Attack on Server

### Starting the flask server

Inside this folder you can launch the server called **app.py** by running command

```
flask run
```

If you access the server now you should be greeted by a bland html page that reads *"Waiting"*.

### I'm in the main frame

Now we can begin the attack. Send the **exploit.zip** through the customer complaint page, and enjoy the results by taking a quick peek at http://localhost:3000/promotion, or whatever the place you are running juice shop at. You should see the login page quickly take over from the video page. 

Now if you input any login credentials and press login, the information is sent to the flask server you should be running most likely at http://localhost:5000/. 

### Where's the juice?

You can verify that the data was sent through two different channels. Take a peek at the CLI running the flask server, and there should be a print of the login information. Alternatively, you can navigate to http://localhost:5000/ and the boring waiting screen has now been replaced by a thank you message from the devious hackers :)

### So what just happened?

We simply replaced the subtitle.vtt file with a html file that you can see as the main.html. This html hides the actual promotion page by using iframes and it is a pretty good copy of Juice Shops login page, albeit not a perfect one, since the google login is disabled as is the show password letters. When the user inputs his email and password to the fields and presses login, the html included in it sends the data over to the flask server.