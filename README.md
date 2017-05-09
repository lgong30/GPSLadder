# Ladder Visualization for L-GPS

This package implements a simple visualization tool for demonstrating the principle of the logarithmic GPS simulator proposed by [Paolo Valente](http://algo.ing.unimo.it/people/paolo/) in [Exact GPS Simulation and Optimal Fair Scheduling with Logarithmic Complexity](http://algo.ing.unimo.it/people/paolo/ToN/L-GPS_ToN.pdf). Note that, the idea here is not totally the same as in the paper, it is actually from one lecture of [Georgia Tech CS7260](http://www.cc.gatech.edu/classes/AY2017/cs7260_spring/), the instructor of which is [Prof. Jun (Jim) Xu](http://www.cc.gatech.edu/~jx/). 


## Install Dependencies

This package depends on the following packages

* flask
* flask_script

You can simply install them by using,

```shell
sudo pip install -r requirements.txt
```

Note, if you want to install it for `Python 3` 
you might need to change `pip` to `pip3`.

## Usage

Go to directory where `GPSLadderctl.py` locates, and open a terminal there, and then type the following shell commands in the terminal:

```shell
python ./GPSLadderctl.py make_tex --help
```

It will show ypu how to manage the options like below,

```shell
usage: GPSLadderctl.py make_tex [-?] [--input INPUT] [--template TEMPLATE]
                                [--template-dir TEMPLATE_DIR]
                                [--output OUTPUT] [--output-dir OUTPUT_DIR]

Generate GPS ladder figure

optional arguments:
  -?, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input data (default: packets.txt)
  --template TEMPLATE, -t TEMPLATE
                        OPTIONAL: template file
  --template-dir TEMPLATE_DIR, -D TEMPLATE_DIR
                        OPTIONAL: directory which stores your template
  --output OUTPUT, -o OUTPUT
                        Output filename (default: example.tex)
  --output-dir OUTPUT_DIR, -d OUTPUT_DIR
                        OPTIONAL: directory to store output file
```

Note that, the input format should be as follows.

```shell
width height
width height
...
```

Here, each line corresponds to a step of the ladder, where `width` is the width of the step, similarly, `height` is the height of the step.

`ladder_data.txt` shows you an example.


## TODO

1. Implement `packet arrival handler`
2. Revise template
