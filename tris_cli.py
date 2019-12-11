# -*- coding:utf-8 -*-
import cmd
import tris

class Cli(cmd.Cmd):

    def __init__(self, boss=None):
        f = open("file.txt", "w")
        cmd.Cmd.__init__(self)
        self.prompt = "tris> "
        self.boss = boss

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

    def emptyline(self):
        print(self.prompt)

    def do_alza(self, line):
        "Alza il motore"
        y = int(line.split()[0])
        tris.alza(y)

    def do_abbassa(self, line):
        "Abbassa il motore"
        y = int(line.split()[0])
        tris.abbassa(y)

    def do_gira_dx(self, line):
        "Gira a destra il motore"
        y = int(line.split()[0])
        tris.gira_a_dx(y)

    def do_gira_sx(self, line):
        "Gira a sinistra il motore"
        y = int(line.split()[0])
        tris.gira_a_dx(y)

    def do_memorizza_pos(self, line):
        "Memorizza la posizione"
        y = int(line.split()[0])
        f.write(str(y))
        print("Posizione salvata")

    def do_end(self):
        f.close()
        do_EOF()

if __name__ == "__main__":

    c = Cli()
    c.run()

# Local Variables:
# tab-always-indent: nil
# tab-width: 4
# End:
