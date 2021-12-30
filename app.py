from os import name
from typing import cast
from flask import Flask
from flask import render_template
import json
import random

app = Flask(__name__)
@app.route("/")

def home():
    # return "Hello, Flask!"

    bts_members = [
        "Jin", 
        "Suga",
        "J-Hope",
        "RM",
        "Jimin",
        "V",
        "Jungkook"
    ]
    bts_members_info = [

        # Jin
        [
            "born December 4",
            "The nickname is worldwide handsome",
            "he is the mom of the group",
            "Jin is also known as that “third guy from the left”",
            "Jin was an exchange student in Australia",
        ], 

        # Suga
        [
            "Suga's favorite color is white",
            "He loves to sleep",
            "know as the savage in the group",
            "his stage names Suga and Agust D,",
            "his liconic line is 'In my next life I want to be born as a rock'"
        ],


        # "J-Hope"
        [
            "He is the Sunshine of the group",
            "He is the main dancer of the group",
            "His iconic line is 'I’m your hope, you’re my hope, I’m Jhope'",
            "J-Hope was a member of the street dance group NEURON.",
            "J-Hope’s motto is “If you don’t work hard, you’ll never get results”."
        ],

        # RM
        [
            "He is the God of Destruction",
            "He is the Leader of the group",
            "His favourite singer was Nas",
            "RM studied in New Zealand and lived there for 6 months.",
            "his iconic line is 'Jimin. You got no jams'"
        ],


        # Jimin
        [
            "Iconic line is Lachimolala",
            "He is famous for little pinky",
            "He is the shortest in the group",
            "In the dorm, Jimin is in charge of the kitchen.",
            "Jimin was ranked 64 places in the “Top 100 Handsome Faces of 2017”"
        ],

        # V
        [
            "His nic name is Tae Tae",
            "He always thinks out of the box",
            "He is also called called an alien",
            "His iconic line is'I'm a GOOD Boy'",
            "He knows how to play the saxophone"
        ],

        # Jungkook
        [
            "He is known as Golden Maknae",
            "He is good at everything",
            "He knows Taekwondo",
            "Jungkook’s favorite color is black ",
            "His iconic line is 'start stage, uh…my heart boom boom'"
        ]
    ]

    rand_no = random.randint(0, len(bts_members)-1)

    img_no = random.randint(1,3)

    member = bts_members[rand_no]

    current_member_info_list = bts_members_info[rand_no]

    info_random_no = random.randint(0, len(current_member_info_list)-1)

    member_info = current_member_info_list[info_random_no]

    return render_template(
        'index.html', 
        current_bias = member,
        # current_number = img_no,
        current_member_info = member_info,
        current_image = f'static/bts_{member}_{img_no}.jpeg',
        current_rand_no = rand_no
    )

@app.route('/flag')
def get_flag():
    rand_no = random.randint(0, 2)
    return render_template(
        'index.html', 
        my_no = rand_no,
        current_image = f'static/bts_{rand_no}.jpeg'
    )

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)