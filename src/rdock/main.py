import subprocess
import re
import time
import os

from htmd import *

class RDock:
    center = [0,0,0]
    radius = 6.0
    protein = "prot.mol2"
    ligand = "lig.mol2"
    nposes = 50

    docked_poses = []

    def set_center(self, center):
        self.center = center

    def set_radius(self, radius):
        self.radius = radius

    # protein in mol2 format
    def set_protein(self, protname):
        if protname.split()[-1] != "mol2":
            print("Invalid protein file - must be mol2")
            
        self.protein = protname

    # ligand in sd format
    def set_ligand(self, ligandname):
        if protname.split()[-1] != "sd":
            print("Invalid ligand file - must be sd")

        self.ligand = ligandname

    def set_nposes(self, nposes):
        self.nposes = nposes

    def generate_input_prm(self):
        content = """RBT_PARAMETER_FILE_V1.00
TITLE input_prm

RECEPTOR_FILE {}
RECEPTOR_FLEX 3.0

SECTION MAPPER
    SITE_MAPPER RbtSphereSiteMapper
    RADIUS {}
    SMALL_SPHERE 1.0
    MAX_CAVITIES 1
    CENTER ({})
END_SECTION

SECTION CAVITY
    SCORING_FUNCTION RbtCavityGridSF
    WEIGHT 1.0
END_SECTION""".format(self.protein, self.radius, ','.join(map(str, self.center)))

        f = open('rdock_input.prm', 'w+')
        f.write(content)
        f.close()
    
    def run_docking(self):
        self.generate_input_prm()

        # generate cavities
        try:
            subprocess.check_output(["rbcavity -was -d -r rdock_input.prm"], shell=True)

        except subprocess.CalledProcessError:
            print("Failed calling rbcavity - Aborting")
            return

        try:
            subprocess.check_output(["rbdock -i {} -o docking_output -r rdock_input.prm -p dock.prm -n {}".format(self.ligand, self.nposes)], shell=True)
        
        except subprocess.CalledProcessError:
            print("Failed calling rbdock - Aborting")
            return

        self.read_docking_results()

    def read_docking_results(self):
        docking_output = open('docking_output.sd', 'r').read()

        allposes = docking_output.split("$$$$")
        for pose in allposes:
            score_regex = re.search('>\s+<SCORE>\n(-?\d+\.\d+)', pose, re.IGNORECASE)
        
            if score_regex:
                self.docked_poses.append([pose, float(score_regex.group(1))])

        #self.docked_poses.sort(key=lambda x: x[1])

        #for dp in self.docked_poses:
        #    print(dp[1])

    def get_best_pose(self):
        poseInfo = self.docked_poses[0]
        tmpFname = 'tmp-{}'.format(int(round(time.time() * 1000)))

        f = open(tmpFname+".sd", 'w+')
        f.write(poseInfo[0])
        f.close()

        # convert with babel to mol2
        subprocess.check_output(["babel -isd {}.sd -omol2 {}.mol2".format(tmpFname, tmpFname)], shell=True)
        mol = Molecule(tmpFname+".mol2")

        os.remove(tmpFname+".sd")
        os.remove(tmpFname+".mol2")

        return mol, poseInfo[1]

if __name__ == '__main__':
    # testing
    rd = RDock()

    rd.set_center([43.9, 9.9, 3.2])
    rd.set_radius(15.0)
    rd.set_protein("prot.mol2")
    rd.set_ligand("ligand.sd")
    rd.set_nposes(50)

    rd.run_docking()
    #rd.read_docking_results()

    pose, score = rd.get_best_pose()
    print(pose, score)