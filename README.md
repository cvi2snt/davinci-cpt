# DAVINCI: A Single-Stage Architecture for Constrained CAD Sketch Inference
### [Ahmet Serdar Karadeniz](https://askaradeniz.github.io/), [Dimitrios Mallis](https://dimitrismallis.github.io/), [Nesryne Mejri](https://www.uni.lu/snt-en/people/nesryne-mejri/), [Kseniya Cherenkova](https://www.linkedin.com/in/kseniya-cherenkova-a3a65a54/), [Anis Kacem](https://www.uni.lu/snt-en/people/anis-kacem/), [Djamila Aouada](https://www.uni.lu/snt-en/people/djamila-aouada/)

#### 🎉 _This work is accepted for publication in [BMVC2024](https://bmvc2024.org/)!!_
#### 📢 _Stay tuned—our dataset and accompanying code will be released soon._

This is the repository for the **CPTSketchGraphs** dataset, a collection of 50 million *Constraint Preserving Transformations (CPTs)* of CAD sketches. CPTs are derived from CAD sketches of the large-scale [SketchGraphs](https://github.com/PrincetonLIPS/SketchGraphs/tree/master) dataset. We aim for **CPTSketchGraphs** to serve as a valuable resource for advancing research in the CAD sketch domain.

![alt text](assets/cpt_figure.png "Examples of Constraint Preservint Transformations (CPTs) of CAD sketches.")

## Constraint Preserving Transformations (CPTs)

Our proposed *Constraint Preserving Transformations (CPTs)*, is a novel augmentation strategy particularly tailored for CAD sketches. CPTs leverage the existing _geometric constraints_ within CAD sketches to generate plausible variations of the original design. 

A random local perturbation, such as the translation of a sketch point, is automatically applied to the CAD sketch. Due to the constraints associated with the manipulated point, this local change cascades across the sketch, modifying the parameterization of all connected primitives. The augmentation process is enabled via integration with the [FreeCAD Python API](https://wiki.freecad.org/FreeCAD_API). 

![alt text](assets/cpt_mechanism.png "The CPT augmentation Strategy")


## Citation
If you use this dataset in your research, please cite:

```
@inproceedings{davinci2024,
    title={DAVINCI: A Single-Stage Architecture for Constrained CAD Sketch Inference},
    author={Ahmet Serdar Karadeniz and Dimitrios Mallis and Nesryne Mejri and Kseniya Cherenkova and Anis Kacem and Djamila Aouada},
    booktitle={British Machine Vision Conference},
    year={2024}
  }
```