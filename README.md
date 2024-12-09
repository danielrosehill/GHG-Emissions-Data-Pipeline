# GHG Emissions Data Pipeline

The function of this repository is to serve as a data pipeline providing CSV data to a number of other projects on my Github repository (specifically those related to visualizing and exploring greenhouse gas emissions data, including through monetizations.) 

The wonderful Streamlit supports ingesting data (dynamically) from data shared on Github which is why this data pipeline is freely accessible. For those looking to use it similarly, the raw data stream for the main CSV (`company_data.csv`) can be found here:

[![CSV](https://img.shields.io/badge/CSV-blue)](https://raw.githubusercontent.com/danielrosehill/GHG-Emissions-Data-Pipeline/refs/heads/main/company_data.csv)

Note: until it's better organised, this data pipeline should be regarded as "first pass" material and is composed from a number of sources.

A second more validated dataset may be added in the future. The purpose of this material is to (ideally) provide *approximately accurate* material to support the exploration of various attempts to visualise the relationship between companies' sustainability performance (with their GHG emissions used as a proxy for that) and their financial performance.

## A Note About Sustainability Data 

Gathering data about companies' greenhouse gas emissions is a complicated and time consuming endeavor. 

The movement in support of greater transparency around companies' social and environmental impacts is a powerful force encouraging the release of such data, typically in the form of PDF documents. 

However, getting from this raw data source to data formatted and optimized for use in data processes is not a simple endeavor. 

The volume of data required to generate reports about greenhouse gas emissions for large organizations is vast. Even the summarized outputs of such initiatives that make it into sustainability disclosures are themselves somewhat complicated.  

My personal belief is that the endeavor of attempting to compare financial performance with sustainability performance is an important one. In recognition of the limits of both my own time and the limited reaches of my abilities to parse this data, some crude methodologies have been applied in an attempt to compare apples against other apples. 

Nevertheless, if this small collection of data can provide a starting point for others investigating ways to visualize and analyze the relationship and correlation between these two data points much will have been achieved. 

## A Note About Verification

In order to avoid infringing upon the copyright of any organization, while it would be possible to do so, the source sustainability reports (where they have been individually analyzed) are not included in this repository. As a workaround of sorts In some cases, and purely for sharing verification of some of these data points links and screenshots of excerpts will be provided. The company list that is populated under data Ssurces is generated programmatically and therefore until they are filled, most of the documents will be empty.

## Repository Map

To avoid confusion, the main data source is provided as a single CSV at the root of the repository. Similarly, a data dictionary is provided as a markdown file at that level. 

In addition to these core files, other files and folders may be added in the future - including perhaps even attempts to organize a pipeline within this pipeline gathering data from other databases through API calls and adding them to the file at the root level.

While enriching the data here with live financial feeds such as those providing stock prices would be highly interesting, I think, doing so is beyond the preview of this project and the technical feasibility of it. Nevertheless, the stock identifiers and tickers are annotated to the companies in order to facilitate precisely that use case in demonstrations, proof of concepts etc.

## Data Dictionary

- `data-dictionary.md`

##  Sources

For those looking for greenhouse gas emissions data which is in the public domain and available at no cost, the following sources can be recommended. 

Note in addition to the limited pool of sources noted here commercial/paid offerings, providing these datapoints to subscribers, exist, for example (among others) the [Sustainalytics Carbon Emissions Dataset](https://www.sustainalytics.com/investor-solutions/esg-research/climate-solutions/carbon-emissions-data) which covers at the time of rating 6000 companies. 

### NZDPU

[![View Website](https://img.shields.io/badge/View%20Website-0077B5?style=flat&logo=link&logoColor=white)](https://nzdpu.com/home)

The Net Zero Data Public Utility provides a centralized repository of company level GHG emissions data. Samples can be navigated and downloaded from the website and the project also provides an API. 

### Open Sustainability Index

[![View Website](https://img.shields.io/badge/View%20Website-0077B5?style=flat&logo=link&logoColor=white)](https://opensustainabilityindex.org)

 Working in partnership with We Don't Have Time, Open Sustainability Index (OSI) provides another open source and free data set listing companies' emissions at the company level. The project also provides an API. Its website includes an AI-backed report data utility which provides automated extraction of financial and emissions parameters from uploaded document data sets. 

---

### Company Emissions Data

[![CSV](https://img.shields.io/badge/CSV-blue)](https://raw.githubusercontent.com/danielrosehill/GHG-Emissions-Data-Pipeline/refs/heads/main/company_data.csv)

## Related Repositories

### GHG Emissions Explorer

[![View on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ghgemissionscalculator.streamlit.app/)

[![Global Value Factors Explorer](https://img.shields.io/badge/Global%20Value%20Factors%20Explorer-Repository-blue?logo=github&style=flat)](https://github.com/danielrosehill/Global-Value-Factors-Explorer)

The Global Value Factors Explorer repository including its visualization on Streamlit is a non official derivative database derived from the Global Value Factors Database as released by the International Foundation for Valuing Impacts in late 2024.

The repository consists of a reformatted version of the database on JSON, CSV, and (forthcoming) GeoJSON intended to streamline the intake of the database for analytical and visualization projects.

---

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).