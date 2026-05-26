from flask import Flask, Response
import time, random

app = Flask(__name__)

BANNER = """
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀(=^･ω･^=)  ⌨️💥💥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀/︶⌨︶\\   *tap tap*⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀|      |⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀|______|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

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
            yield "\033[2J\033[H" + msg + "\n\n" + BANNER
            time.sleep(10)
    return Response(gen(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
