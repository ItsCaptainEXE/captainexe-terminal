from flask import Flask, Response
import time, random

app = Flask(__name__)

BANNER = r"""
print("yup yup finishing my coffee")

          (=^･ω･^=)  💻💥💥
            /   \      *tap tap*
            |   |      
            |___|

                          @ItsCaptainEXE
          captainexe.live • github.com/ItsCaptainEXE
"""

MESSAGES = [
    'print("loaaaaaaaaaaaaaaaadddddddddddddddiiiiiiiiiiinnnnnnnnnnnnngggggggg")',
    'print("i might be ignoring you")',
    'print("hello internet")',
    'print("still here?")',
    'print("yup yup finishing my coffee")'
]

@app.route("/")
def stream():
    def gen():
        while True:
            msg = random.choice(MESSAGES)
            # clear screen + move cursor home
            yield "\033[2J\033[H" + msg + "\n\n" + BANNER + "\n"
            time.sleep(2.3)  # <- 2.3 seconds
    return Response(gen(), mimetype="text/plain")

if __name__ == "__main__":
    # Railway uses Procfile in production, this is just for local runs
    app.run(host="0.0.0.0", port=8080)
