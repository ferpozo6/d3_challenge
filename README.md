# Protein-ligand docking protocol

* `output_best_poses` contains the best poses that we got for our first 10 ligands
* `src` folder contains helper classes (rdock, parameterize, babel)
* `project_data` contains necessary data to run the python notebook (apoprotein, ligands)
* `build_ligand_1` is a script to run equilibration and preparation for 3 best poses (by AutoDock, rDock and SwissDock) with htmd
* Main project is `D3Challenge.ipynb`

## Install from Conda
```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh
conda create -n autodocking python=3
conda activate autodocking
https://github.com/fpozoc/d3_challenge.git
cd d3_challenge 
conda env create -f ./environment.yml
jupyter-lab
```

## Release History

* 0.1.0
    * Building

## Meta

Fernando Pozo - [@fpozoca](https://twitter.com/fpozoca) - fpozoc@cnio.es

Distributed under the GNU General Public License. See ``LICENSE`` for more information.

[https://github.com/ferpozo6](https://github.com/ferpozo6)

Originally it was created from a collaborative project [https://github.com/novikk/d3_challenge](https://github.com/novikk/d3_challenge) to participate in the [D3 Challenge](https://drugdesigndata.org/about/challenge-pl-2016-1)[]

## Contributing

1. Fork it (<https://github.com/fpozoc/d3_challenge>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request