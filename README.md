## Introduction  

Glyco-PAINT is a research method to study interactions of glycans on lectins on live cells. The Glyco-PAINT Application Processing Pipeline is a software solution to process and analyse experimental results.

## Reference
The software and selected research results are described in:  

> Steuten, K., Bakker, J.J.A., Doelman, W. et al. Subcellular glycan-mannose receptor binding kinetics correlate with myeloid cell function. Nat Commun 17, 886 (2026). https://doi.org/10.1038/s41467-025-67602-x  

The Pipeline, presented here, is a research application to extract information from the GlycoPaint recordings. The pipeline is a collection of Python and R scripts and depends heavily on the Glyco-PAINT method, Fiji and TrackMate.

> Riera, R., Hogervorst, T.P., Doelman, W. et al. Single-molecule imaging of glycan–lectin interactions on cells with Glyco-PAINT. Nat Chem Biol 17, 1281–1288 (2021). https://doi.org/10.1038/s41589-021-00896-2
> 
> Ershov, D., Phan, M.-S., Pylvänäinen, J. W., Rigaud, S. U., Le Blanc, L., Charles-Orszag, A., … Tinevez, J.-Y. (2022).
TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines. Nature Methods, 19(7),
829–832. doi:10.1038/s41592-022-01507-1

## Software environment 
The software has been tested on a MacBook with MacOS 14 (Intel) and 15 (Arm), on a Windows 10 and 11. 

## System requirements
No special system requirements are identified, other than a minimum memory of 16GB. More memory and a fast processor will reduce runtimes. 

## Installation
To assist with installing the components of the pipeline, [Installation instructions](doc/Installation.md) are provided.

## License
The software is provided as is under the [MIT license](LICENSE).

## Functionality
An overview of the functionality of the pipeline, how to use it and a detailed demo case with sample data it is provided in the [Paint Pipeline Documentation](doc/Paint_Pipeline_Documentation.md).

## Sample image data 
Sample image data is provided on Zenodo: https://doi.org/10.5281/zenodo.14196381. This data can be used to run the demonstration case described in [Paint Pipeline Documentation](doc/Paint_Pipeline_Documentation.md).
