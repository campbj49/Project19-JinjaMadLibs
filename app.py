from flask import Flask, request, render_template
from stories import *
#from jinja2 import *

app = Flask(__name__)
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route("/")
def start():
    not_submitted = request.args.get(story.prompts[0],"not_checked") == "not_checked"
    
    filled_template = story.generate(request.args)
    
    return render_template("start.html", 
        title="Beginning",  
        header="Prompts", 
        prompts=story.prompts,
        not_submitted=not_submitted,
        story= filled_template)
        
@app.route("/story")
def story_output():
    return render_template("story.html",
        title="Story",
        header="header")