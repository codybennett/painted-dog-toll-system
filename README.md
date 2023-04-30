<!-- This README was created and based off of https://github.com/othneildrew/Best-README-Template -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<h3 align="center">Painted Dog Toll System</h3>

  <p align="center">
    Proof of Concept Toll System for Painted Dog Research Trust
    <br />
    <a href="https://github.com/cody-bennett/painted-dog-toll-system/issues">Report Bug</a>
    ·
    <a href="https://github.com/cody-bennett/painted-dog-toll-system/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to create a tollbooth style system that operates similar to a clock-in/clock-out attendance system. This allows local enforcement of time based repercussions to speeding violations. 

At its core, the project will:
* Clock-in an RFID card issued to a driver at the entrance of a toll zone
* Clock-out the previously issued RFID card at the exit of the toll zone
* Calculate average speed over the predefined distance
* Output a "timeout" period for the driver based on whether or not, and how much, the driver may have been speeding by utilizing the calculated velocity 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is designed to run on a RaspberryPi with a RFID RC522 reader and writer.

Instructions for doing so can be found (at the time of this writing) at [Pi My Life Up](https://pimylifeup.com/raspberry-pi-rfid-rc522/)

This utilizes a local MySQL/MariaDB database, the schema is included and located at [painted_dog_db.sql](painted_dog_db.sql)

### Prerequisites

Either a local or remote MySQL compatible database may be used, for practical purposes a remote database will be ideal to enforce synchronization between RaspberryPi nodes

Import MySQL/MariaDB Database
 ```mysql
 mysql -u <user> -p < painted_dog_db.sql
 ```

### Installation

1. Install and configure [pipenv](https://pipenv.pypa.io/en/latest/)
2. Clone the repo
   ```sh
   git clone https://github.com/cody-bennett/painted-dog-toll-system.git
   ```
3. Install Python packages
   ```sh
   pipenv install
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Currently, this works on a local proof of concept mode and requires some manual data entry.

[trafficsimulator.py](trafficsimulator.py) contains the code that will be running the Toll System and updating the database records accordingly. 

This module contains a distance variable for providing the applicable distance for calculating velocity. 
| This is something that will need to be modularized and parameterized

After configuring the RFID reader/writer and the Python environment, execute [trafficsimulator.py](trafficsimulator.py) which will start the program.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Frond End Application
- [ ] Remote Database Implementation
- [ ] Modular Inputs
    - [ ] Touch Screen Based Inputs

See the [open issues](https://github.com/cody-bennett/painted-dog-toll-system/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Cody Bennett: [LinkedIn](https://www.linkedin.com/in/cody-bennett-2087467b/)

Project Link: [https://github.com/cody-bennett/painted-dog-toll-system](https://github.com/cody-bennett/painted-dog-toll-system)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cody-bennett/painted-dog-toll-system.svg?style=for-the-badge
[contributors-url]: https://github.com/cody-bennett/painted-dog-toll-system/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cody-bennett/painted-dog-toll-system.svg?style=for-the-badge
[forks-url]: https://github.com/cody-bennett/painted-dog-toll-system/network/members
[stars-shield]: https://img.shields.io/github/stars/cody-bennett/painted-dog-toll-system.svg?style=for-the-badge
[stars-url]: https://github.com/cody-bennett/painted-dog-toll-system/stargazers
[issues-shield]: https://img.shields.io/github/issues/cody-bennett/painted-dog-toll-system.svg?style=for-the-badge
[issues-url]: https://github.com/cody-bennett/painted-dog-toll-system/issues
[license-shield]: https://img.shields.io/github/license/cody-bennett/painted-dog-toll-system.svg?style=for-the-badge
[license-url]: https://github.com/cody-bennett/painted-dog-toll-system/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/cody-bennett-2087467b/
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/github/pipenv/locked/python-version/cody-bennett/painted-dog-toll-system
[Python-url]: https://python.org/

