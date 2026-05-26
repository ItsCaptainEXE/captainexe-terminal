from flask import Flask, Response
import time, random

app = Flask(__name__)

# Catppuccin Mocha purple
PURPLE = "\033[38;2;203;166;247m"
WHITE = "\033[97m"
RESET = "\033[0m"

BANNER = rf"""
{WHITE}

          (=^･ω･^=)  💻💥💥
            /   \      *tap tap*
            |   |      
            |___|

                          @ItsCaptainEXE
          captainexe.live • github.com/ItsCaptainEXE{RESET}
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

    # funnier ones
    'print("loading… probably")',
    'print("this is fine. everything is fine.")',
    'print("your patience is being monitored")',
    'print("fun fact: this message does nothing")',
    'print("hold on, recalibrating the flux capacitor")',
    'print("optimizing… for dramatic effect")',
    'print("loading the loading screen…")',
    'print("please do not turn off your human")',
    'print("processing your vibe…")',
    'print("booting the cat…")',
    'print("compiling patience.exe")'
]

@app.route("/")
def stream():
    def gen():
        while True:
            msg = random.choice(MESSAGES)

            # FULL CLEAR + CURSOR HOME
            clear = "\033[2J\033[H"

            # Purple message + white banner
            screen = (
                clear +
                PURPLE + msg + RESET + "\n\n" +
                BANNER + "\n"
            )

            yield screen
            time.sleep(2.3)

    return Response(gen(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
