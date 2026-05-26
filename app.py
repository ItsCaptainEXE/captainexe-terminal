from flask import Flask, Response
import time, random

app = Flask(__name__)

BANNER = r"""
print("yup,yup just finishing my coffee")

          (=^･ω･^=)  💻💥💥
            /   \      *tap tap*
            |   |      
            |___|

                          @ItsCaptainEXE
          captainexe.live • github.com/ItsCaptainEXE
"""

MESSAGES = [
    'print("will this ever load?")',
    'print("still here?")',
    'print("please email me if you are stuck here")',
    'print("if you click random things you may find a secret feature")',
    'print("loaaaaaaaaaaaaaaaadddddddddddddddiiiiiiiiiiinnnnnnnnnnnnngggggggg")',
    'print("hello internet")',
    'print("if you are here too long buy more RAM")',
    'print("i mean its still faster than a windows update")',
    'print(":D")',
    'print("in case you activate a secret easter egg press ` to stop this — just kidding")',
    'print("i mean im gonna take my time")',
    'print("yup,yup just finishing my coffee")',
    'print("i might be ignoring you")',

    'print("loading… probably")',
    'print("this is fine. everything is fine.")',
    'print("your patience is appreciated. by me. only me.")',
    'print("fun fact: this message is completely useless")',
    'print("if this loads, you win absolutely nothing")',
    'print("hold on, recalibrating the flux capacitor")',
    'print("optimizing… for dramatic effect")',
    'print("loading the loading screen…")',
    'print("please do not turn off your human")',
    'print("processing your vibe…")',
    'print("booting the cat…")',
    'print("compiling your patience.exe")'
]

@app.route("/")
def stream():
    def gen():
        while True:
            msg = random.choice(MESSAGES)
            yield "\033[2J\033[H" + msg + "\n\n" + BANNER + "\n"
            time.sleep(2.3)
    return Response(gen(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
