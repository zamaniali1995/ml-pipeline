<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url] -->
<!-- [![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Machine Learning Pipeline Template</h3>

  <p align="center">
    A useful template to utilize for simple and efficient machine learning projects
    <br />
    <a href="https://github.com/zamaniali1995/ml-pipeline"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo (TO BE COMPLETED)</a>
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
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

<!-- This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

<!-- * [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=Python&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Sklearn-informational?style=flat&logo=Sklearn&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Numpy-informational?style=flat&logo=Numpy&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Scipy-informational?style=flat&logo=Scipy&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Package-Pandas-informational?style=flat&logo=Pandas&logoColor=white&color=4AB197)
![](https://img.shields.io/badge/Framework-Flask-informational?style=flat&logo=Flask&logoColor=white&color=4AB197)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here we will describe the necessary actions and steps that should be followed in order to run this pipeline.

### Prerequisites

We have only a couple of prerequisite steps required to run this pipeline. The first of which is to have Conda or Anaconda installed and the second is to be able to utilize MakeFiles.


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

If there is a desire to implement some additional processing method or some specific functionality for a given dataset, we have created an simple process to add utility functions that can be used and connected with the configuration files easily.


### Running Each Step

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
<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Develop Base Pipeline Template
- [x] Implement Example Dataset and Functional Front-End
- [ ] Add additional data processing utility functions to be available for use.
- [ ] Implement Test-Cases to be used for validation of the different pipeline steps
- [ ] Add more ways to load data
  - [ ] AWS
  - [ ] Google Cloud
  - [ ] Microsoft Azure

See the [open issues](https://github.com/zamaniali1995/ml-pipeline/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Ali Zamani - [LinkedIn](https://www.linkedin.com/in/zamaniali1995/) - azamani1@ualberta.ca

Jacob Mish - [LinkedIn](https://www.linkedin.com/in/jacob-mish-25915722a/) - JacobPMish@gmail.com

Project Link: [https://github.com/zamaniali1995/ml-pipeline](https://github.com/zamaniali1995/ml-pipeline)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
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

