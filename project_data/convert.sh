#!/bin/sh

# split sdf file into 1 sdf file per ligand
awk '
/FXR_/ {close(fname); fname=sprintf("ligand_FXR_%d.sdf", ++sdfcount)}
	{print >fname}
' ALL_FXR_compounds_D3R_GC2.sdf

# remove ligands > 36 (we only want 36 first ligands)
#find . -name 'ligand_*' | while read file; do
#	[ "${${file#./ligand_FXR_}%.sdf}" -gt 36 ] && rm -v "$file"
#done

# convert from sdf to 3d protonated mol2 file
for i in ligand_*.sdf; do
 	babel -isdf $i -omol2 $i.mol2 -h --gen3D
	parameterize -m $i.mol2 --no-min --no-esp --no-torsions -o ./param-$i
done

