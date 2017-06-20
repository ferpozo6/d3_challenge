import subprocess

''' Helper class to call parameterize '''
class Parameterize:
    params = {}
    mol = "mol.mol2"
    out = "./params"

    def set_input(self, input):
        self.mol = input

    def set_output(self, output):
        self.out = output

    def no_torsions(self):
        self.params["--no-torsions"] = True

    def no_min(self):
        self.params["--no-min"] = True

    def no_esp(self):
        self.params["--no-esp"] = True

    def run(self):
        return subprocess.check_output(["parameterize -m {} {} -o {}".format(
            self.mol,
            ' '.join(self.params.keys()),
            self.out
        )], shell=True)

if __name__ == '__main__':
    p = Parameterize()
    p.set_input("test.mol2")
    p.set_output("./params-test")

    p.no_esp()
    p.no_min()
    p.no_torsions()

    p.run()