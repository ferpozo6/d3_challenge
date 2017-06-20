import subprocess

''' Helper class to call open babel '''
class Babel:
    input_file = "mol.pdb"
    output_file = "mol.mol2"

    protonate = False

    def set_input_file(self, ifile):
        self.input_file = ifile

    def set_output_file(self, ofile):
        self.output_file = ofile

    def protonate(self, p):
        self.protonate = p

    def run(self):
        input_type = self.input_file.split(".")[-1]
        output_type = self.output_file.split(".")[-1]

        callFunc = "babel -i{} {} -o{} {}".format(
            input_type, self.input_file,
            output_type, self.output_file
        )

        if self.protonate:
            callFunc += " -h"

        return subprocess.check_output(callFunc, shell=True)

if __name__ == '__main__':
    b = Babel()
    b.set_input_file("test.mol2")
    b.set_output_file("test.sd")

    b.protonate(True)

    b.run()