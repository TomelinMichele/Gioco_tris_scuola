# -*- coding:utf-8 -*-
import cmd
import tris

import os.path
try:
    import readline
except ImportError:
    readline = None

hist_file = os.path.expanduser('~/.tris_history')
hist_file_size = 1000

pos_file = "motor_pos.txt"
cur_pos = [0,0,0]
all_pos = dict()

class Cli(cmd.Cmd):

    def __init__(self, boss=None):
        cmd.Cmd.__init__(self)
        self.prompt = "tris> "
        self.boss = boss
        try:
            tris.init()
        except Exception as e:
            print(f"tris.init() FAILED with {e}")

    def do_save_pos(self, line):
        with open(pos_file, "w") as f:
            for k,v in all_pos.items():
                v = " ".join(map(str, v))
                f.write(f"{k} {v}\n")

    def do_show_pos(self, line):
        s = line and line.split()[0] or ""
        with open(pos_file) as f:
            for r in f:
                k, *v = r.split()
                if not s or s == k:
                    print(r)

    def preloop(self):
        if readline and os.path.exists(hist_file):
            readline.read_history_file(hist_file)

    def postloop(self):
        if readline:
            readline.set_history_length(hist_file_size)
            readline.write_history_file(hist_file)

    def onecmd(self, line):
        try:
            return super().onecmd(line)
        except Exception as e:
            print(f"ERROR: {e}")
            return False # don't stop

    def run(self):
        self.cmdloop()

    def do_EOF(self, line):
        print("bye")
        return True

    do_end = do_EOF             # alias for EOF/CRTL-d

    def emptyline(self):
        print(self.prompt)

    def do_alza(self, line):
        "Alza il motore"
        y = int(line.split()[0])
        cur_pos[0] += y
        tris.alza(y)

    def do_abbassa(self, line):
        "Abbassa il motore"
        y = int(line.split()[0])
        cur_pos[0] -= y
        tris.abbassa(y)

    def do_ruota_interno(self, line):
        "Gira a destra il motore"
        y = int(line.split()[0])
        cur_pos[1] += y
        tris.ruota_interno(y)

    def do_ruota_esterno(self, line):
        "Gira a sinistra il motore"
        y = int(line.split()[0])
        cur_pos[2] += y
        tris.ruota_esterno(y)

    def do_memorizza_pos(self, line):
        "Memorizza la posizione"
        global cur_pos
        motor = line.split()[0]
        # tris.memorizza_pos(motor)
        print(f"Posizione {motor} {cur_pos} salvata")
        all_pos[motor] = cur_pos
        cur_pos = [0,0,0]

    def complete_lamp(self, text, line, begidx, endidx):
        ss = "lamp_rossa lamp_verde lamp_pareggio lamp_vince_robot lamp_vince_umano".split()
        oo = line.split()
        text = oo[-1]
        if len(oo) == 2 and line[-1].strip():
            ww = "lamp_rossa lamp_verde lamp_pareggio lamp_vince_robot lamp_vince_umano"
        elif len(oo) == 3:      # TODO FIX THIS
            ww = "on off"
        ss = ww.split()
        if not text:
            return ss.copy()
        cc = [s for s in ss if s.startswith(text)]
        return cc

    def do_lamp(self, line):
        lamp, state = line.split()
        print(f"tris.lamp({lamp}, {state})")
        tris.lamp(lamp, state)

if __name__ == "__main__":

    c = Cli()
    c.run()
