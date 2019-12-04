# -*- coding:utf-8 -*-
import cmd
# import tris

class Cli(cmd.Cmd):

    def __init__(self, boss=None):
        f = open("file.txt", "w")
        cmd.Cmd.__init__(self)
        self.prompt = "tris>"
        self.boss = boss
    
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
        print("alza %d" % y)
     
    def do_abbassa(self, line):
        "Abbassa il motore"
        y = int(line.split()[0])
        print("abbassa %d" % y)
     
    def do_gira_dx(self, line):
        "Gira a destra il motore"
        y = int(line.split()[0])
        print("Gira %d" % y)
       
   def do_gira_sx(self, line):
        "Gira a sinistra il motore"
        y = int(line.split()[0])
        print("Gira %d" % y)
        
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
