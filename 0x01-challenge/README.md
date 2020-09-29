# 0x01. Fix my code

Fix my code is a new type of project, where we’ll jump into an existing code base and fix it!

Sometime you will know the language, sometime not.

Please download the repository 0x01-Fix_My_Code_Challenge and use it as initial files for all solutions.

You should not recode everything, just fix it!

### [0. Server status](./status_server/)
* I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).
But I don’t know why it’s not working…

Could you look at it and fix it please?

My code is here
```
$ python -m api.v1.app 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
```
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```

### [1. My square](./square.py)
* I love geometry! 
Look my square, it’s perfect? No? Should I change something?

### [2. Step 2: User model](./user.py)
* I’m running into a serious problem! 
I just start my OOP project and nothing works…

Could you help me please? My code is here.

Thank you!

### [3. Blog access](./blog)
* I finished and deployed my Rails blog but people are contacting me because they can’t access any of my blog posts… Weird, it works for me…
Could you take a look and fix it? My code base is here.

Also, when you’re done, could you add a new feature please?

I would like to add a boolean online for each Post object with a default value true. With this boolean, I will be able to hide/show some blog posts from the listing. I will also need a way to change this boolean in the Post#edit route. Could you do this for me?

Thank you!

### [4. Never leave the office](./react-blog)
* I’m coming back from 2 weeks of holidays in France and when I arrived at the office, the first words from my marketing co-worker were: “Hi, how was your holiday? by the way, I think I broke the website…”
WHAT???

Ok, let’s jump on it and fix it!

Arf, I have also the pagination to fix… I didn’t have time before my break to look at it…

---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)