<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Machine Learning Pipeline Template</h3>

  <p align="center">
    A useful template to enable simple and efficient machine learning projects
    <br />
    <a href="https://github.com/zamaniali1995/ml-pipeline"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://zamaniali1995.pythonanywhere.com/">View Demo</a>
    ·
    <a href="https://github.com/zamaniali1995/ml-pipeline/issues">Report Bug</a>
    ·
    <a href="https://github.com/zamaniali1995/ml-pipeline/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    <li><a href="#directory-information">Directory Information</a></li>
      <ul>
        <li><a href="#app">App</a></li>
        <li><a href="#config">Config</a></li>
        <li><a href="#pipeline-components">Pipeline Components</a></li>
        <li><a href="#src">Src</a></li>
      </ul>
    </li>
    <li><a href="#built-with">Built With</a></li>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]


While developing our machine learning pipeline template, we wanted to create an efficient and purposeful environment that could resolve many of the annoyances and issues we have faced in the past.

Our goal with this ML pipeline template is to create a user friendly utility to drastically speed up the development and implementation of a machine learning model for all sorts of various problems. Many of our past experiences with other templates or machine learning projects had left us hoping for a better working environment and a more efficient process. 

This template enables fast experimentation, easy execution, and simple debugging for all components. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Directory Information
### **app/**
   ```sh
  .
  ├── run.py                        # Python remote server control
  ├── static
  │   └── img
  │       ├── example_image.jpg     # Example image for README
  │       ├── iris_setosa.jpeg
  │       ├── iris_versicolor.jpeg
  │       └── iris_virginica.jpeg
  └── templates
      ├── go.html
      └── master.html                 # Main html file for front end
   ```

The *app* component of the directory controls the front end flask service which produces the user-friendly environment for interacting with the model.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### **config/**
   ```sh
  .
  ├── config.yaml           # Main global configuration file 
  ├── data_acquisition      
  │   └── config.yaml       # Data acquisition configuration 
  ├── data_processing
  │   └── config.yaml       # Data processing configuration
  ├── model_training
  │   └── config.yaml       # Model training configuration 
  └── model_validation
      └── config.yaml       # Model validation configuration
   ```

The *config* component of the directory is where the most controls reside for this pipeline template. There is a config file for each of the main sections:

* **Data Acquisition**
* **Data Processing**
* **Model Training**
* **Model Validation**

There is also an additional configuration file for general settings that relate to each of these different sections and are shared. 

The configuration files are intended to be the primary point of access and control for this pipeline. Any changes or utility additions should be controlled from their corresponding configuration file in order to keep an organized and properly modularized codebase.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### **pipeline_components/**
   ```sh
  .
  ├── 1_data_acquisition
  │   └── main.py         # Main file for data acquisition step
  ├── 2_data_processing
  │   └── main.py         # Main file for data processing step
  ├── 3_model_training
  │   └── main.py         # Main file for model training step
  ├── 4_model_validation
  │   └── main.py         # Main file for model validation step
  └── 5_model_registration
      └── main.py         # Main file for model registration step (Optional)
   ```

The *pipeline_components* folder in the directory is the host to the main files for each step in the pipeline flow. Here, there exist only main files for each step (ordered numerically to represent the order of runtime). These main files should not be altered unless required to implement an additional utility function or some other task. Changes made to this pipeline should remain within the utility functions in the /src/ directory and in the configuration files.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### **src/**
   ```sh
.
├── __init__.py   
├── data
│   ├── __init__.py
│   ├── acquisition     
│   │   ├── __init__.py
│   │   └── utils.py    # Data acquisition utility functions
│   ├── processing
│   │   └── utils.py    # Data processing utility functions
│   └── utils.py        # General utility functions related to data
├── model
│   ├── __init__.py
│   ├── training
│   │   ├── __init__.py
│   │   └── utils.py    # Data model training utility functions
│   └── utils.py        # General utility functions related to models
└── utils.py            # Main general utility functions
   ```

The *src* component of the directory is the core of our pipelines functionality. This directory stores the utility functions for each of the pipeline steps. When running the pipeline, these utility functions will be built as a package and can be imported and used in the main functions during runtime. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=Python&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Sklearn-informational?style=flat&logo=Sklearn&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Numpy-informational?style=flat&logo=Numpy&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Scipy-informational?style=flat&logo=Scipy&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Pandas-informational?style=flat&logo=Pandas&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Framework-Flask-informational?style=flat&logo=Flask&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Style-HTML-informational?style=flat&logo=Html&logoColor=white&color=4AB197)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here we will describe the necessary actions and steps that should be followed in order to run this pipeline.

### Prerequisites

There are only a couple of prerequisite steps required to run this pipeline. The first of which is to have Conda / Anaconda installed and the second is to be able to utilize MakeFiles.


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/zamaniali1995/ml-pipeline.git
   ```
2. Setup the conda environment using MakeFile
   ```make
   make create-env
   ```
3. Activate the newly created conda environment
   ```make
   conda activate test-env
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Here we will describe how to use this ML pipeline template, as well as how to run each component and build the front end display at the end.

This pipeline was designed so that configuration files are the primary means of controlling and altering the pipeline. These configuration files control the paths to the data, what kind of data processing to perform, how to split the training and testing data, which models to train, the range of potential hyper parameters to search through, which evaluation methods to use on the models, and many other similar selections.

These configuration files allow for changes to be made in one place, not requiring someone to dig through code and alter each place where some variable could exist. 

If there is a desire to implement some additional processing method or some specific functionality for a given dataset, we have created a simple process to add utility functions that can be used and connected with the configuration files easily.


### **Running Each Step**

To validate that our template is working, we have included a sample dataset which can be used to run each component of the pipeline and which will produce a useable front-end local server. If everything is working as intended, the following steps should be able to produce a functioning predictor.

1. Acquire the data
   ```make
   make acquire-data
   ```
2. Process the data
   ```make
   make process-data
   ```
3. Train the model
   ```make
   make train-model
   ```
4. Evaluate the model
   ```make
   make evaluate-model
   ```
5. Generate the local Flask front-end
   ```make
   make run-server
   ```
6. Access the local Flask server
   ```https
   http://localhost:3001/
   ```
   or

   ```https
   http://0.0.0.0:3001/
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Develop Base Pipeline Template
- [x] Implement Example Dataset and Functional Front-End
- [ ] Add additional data processing utility functions to be available for use.
- [ ] Implement Test-Cases to be used for validation of the different pipeline steps
- [ ] Run the whole pipeline with one single command like run-pipeline
- [ ] Add more ways to load data
  - [ ] AWS
  - [ ] Google Cloud
  - [ ] Microsoft Azure

See the [open issues](https://github.com/zamaniali1995/ml-pipeline/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License



<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Ali Zamani - [LinkedIn](https://www.linkedin.com/in/zamaniali1995/) - azamani1@ualberta.ca

Jacob Mish - [LinkedIn](https://www.linkedin.com/in/jacob-mish-25915722a/) - JacobPMish@gmail.com

Project Link: [https://github.com/zamaniali1995/ml-pipeline](https://github.com/zamaniali1995/ml-pipeline)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments


<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/zamaniali1995/ml-pipeline/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: app/static/img/example_image.jpg
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 


<!-- # Tasks
- [ ] Load data from Azure
- [ ] Load data from AWS
- [ ] Load data from Google Cloud
- [ ] Add more methods for feature extraction
- [x] Add EDA -> Ali
- [ ] Add test
- [x] Model selection and hyperparameter tunning -> Ali
- [x] Save the best model -> Ali
- [x] Save the best model trained on whole dataset -> Ali
- [x] Complete model evaluation -> Ali
- [x] Complete front-end -> Ali
- [x] Complete docstring -> Jacob
- [ ] Complete Read.ME -> Jacob -->

