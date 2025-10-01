from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import x 
import time
import uuid
import os

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

app = Flask(__name__)

# Set the maximum file size to 10 MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024   # 1 MB

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
 

##############################
##############################
##############################
def _____USER_____(): pass 
##############################
##############################
##############################

@app.get("/")
def view_index():
   
    return render_template("index.html")

##############################
@app.get("/login")
def view_login():
    if session.get("user", ""): return redirect(url_for("view_home"))

    message = request.args.get("message", "")
    return render_template("login.html", message=message)

##############################
@app.get("/ajax")
def view_ajax():
    try:
        return render_template("ajax.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/ajax-heart")
def view_heart_heart():
    try:
        return render_template("ajax_heart.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/api-like-tweet")
def api_like_tweet():
    try:
        # TODO: Validate the data
        # TODO: Get the logged user id
        # TODO: Connect to the database
        # TODO: Disconnect from the database
        # TODO: Insert the liking of a tweet in the table
        # TODO: Check that everything went as expected
        # TODO: Reply to the browser informing that the tweet is liked

        return {"status":"oki doki"}
    except Exception as ex:
        ic(ex)
        return {"status":"error"}
    finally:
        pass

##############################
@app.get("/api-unlike-tweet")
def api_unlike_tweet():
    try:
        # TODO: Validate the data
        # TODO: Get the logged user id
        # TODO: Connect to the database
        # TODO: Disconnect from the database
        # TODO: Delete the liking of a tweet in the table
        # TODO: Check that everything went as expected
        # TODO: Reply to the browser informing that the tweet is liked

        return {"status":"oki doki"}
    except Exception as ex:
        ic(ex)
        return {"status":"error"}
    finally:
        pass

##############################
@app.get("/ajax-post")
def view_post_ajax():
    try:
        return render_template("ajax_post.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/ajax-bookmark")
def view_post_ajax_bookmark():
    try:
        return render_template("ajax_bookmark.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/items")
def view_items():
    try:
        next_page = 1
        items_per_page = 2
        offset = 0

        db, cursor = x.db()
        q = "SELECT * FROM posts LIMIT %s, %s"
        cursor.execute(q, (offset, items_per_page))
        items = cursor.fetchall()
        ic(items)

        return render_template("items.html", items=items, next_page=next_page)
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/api-get-items")
def api_get_items():
    try:
        next_page = int(request.args.get("page", "0"))
        items_per_page = 2
        offset = next_page * items_per_page
        ic(next_page, offset)

        db, cursor = x.db()
        q = "SELECT * FROM posts LIMIT %s, %s"
        cursor.execute(q, (offset, items_per_page))
        items = cursor.fetchall()
        ic(items)

        container = ""
        for item in items:
            html_item = render_template("_item.html", item=item)
            container = container + html_item
        ic(container)
        #new_hyperlink = render_template("___show_more.html", next_page=next_page+1)

        new_hyperlink = ""
        if len(items) == items_per_page:
            new_hyperlink = render_template("___show_more.html", next_page=next_page + 1)


        return f"""
            <mixhtml mix-bottom="#items_container">
                {container}
            </mixhtml>
            <mixhtml mix-replace="#show_more">
                {new_hyperlink}
            </mixhtml>
        """
        # return render_template("items.html", items=items)
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.post("/save")
def api_save():
    try:
        user_name = request.form.get("user_name", "give me a name")
        user_last_name = request.form.get("user_last_name")
        user_nick_name = request.form.get("user_nick_name")

    # Dictionary in python is JSON in JavaScript
        user = {
            "user_name" : user_name.upper(),
            "user_last_name" : user_last_name.upper(),
            "user_nick_name" : user_nick_name.upper()
        }

        return user
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.post("/api-bookmark")
def api_bookmark():
    try:
        return """
        <mixhtml mix-replace='button'>
            <button mix-post="/api-remove-bookmark">
                <i class="fa-solid fa-bookmark"></i>
            </button>
        </mixhtml>

        <mixhtml mix-before="button">
            <div mix-ttl="5000" mix-fade-out>I will disappear</div>
        </mixhtml>
        """
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/tweet")
def api_tweet():
    try:
        return "You pissed yourself!"
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.post("/login")
def handle_login():
    try:
        # Validate
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        # Connect to the database
        q = "SELECT * FROM users WHERE user_email = %s"
        db, cursor = x.db()
        cursor.execute(q, (user_email,))
        user = cursor.fetchone()
        if not user: raise Exception("User not found", 400)

        if not check_password_hash(user["user_password"], user_password):
            raise Exception("Invalid credentials", 400)

        user.pop("user_password")

        session["user"] = user
        return redirect(url_for("view_home"))

    except Exception as ex:
        ic(ex)
        if ex.args[1] == 400: return redirect(url_for("view_login", message=ex.args[0]))
        return "System under maintenance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/signup")
def view_signup():
    message = request.args.get("message", "")
    return render_template("signup.html", message=message)

##############################
@app.post("/signup")
def handle_signup():
    try:
        # Validate
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_username = x.validate_user_username()
        user_first_name = x.validate_user_first_name()

        user_hashed_password = generate_password_hash(user_password)

        # Connect to the database
        q = "INSERT INTO users VALUES(%s, %s, %s, %s, %s)"
        db, cursor = x.db()
        cursor.execute(q, (None, user_email, user_hashed_password, user_username, user_first_name))
        db.commit()
        return redirect(url_for("view_login", message="Signup successful. Proceed to login"))
    except Exception as ex:
        ic(ex)
        if ex.args[1] == 400: return redirect(url_for("view_signup", message=ex.args[0]))
        if "Duplicate entry" and user_email in str(ex): return redirect(url_for("view_signup", message="Email already registered"))
        if "Duplicate entry" and user_username in str(ex): return redirect(url_for("view_signup", message="username already registered"))
        return "System under maintenance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()


##############################
@app.get("/home")
@x.no_cache
def view_home():
    try:
        db, cursor = x.db()
        
        q = "SELECT * FROM users JOIN posts ON user_pk = post_user_fk ORDER BY RAND() LIMIT 5"
        cursor.execute(q)
        rows = cursor.fetchall()
        ic(rows)

        qTrend = "SELECT * FROM trending ORDER BY RAND() LIMIT 4"
        cursor.execute(qTrend)
        trending_rows = cursor.fetchall()
        ic(trending_rows)
        
        qFollow = "SELECT * FROM users ORDER BY RAND() LIMIT 3"
        cursor.execute(qFollow)
        users_rows = cursor.fetchall()
        ic(users_rows)

        # user = session.get("user", "")
        # if not user: return redirect(url_for("view_login"))
        return render_template("home.html", rows=rows, trending_rows=trending_rows, users_rows=users_rows)
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()



##############################
@app.get("/logout")
def handle_logout():
    try:
        session.clear()
        return redirect(url_for("view_login"))
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass
















