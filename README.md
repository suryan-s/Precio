
![Banner](https://user-images.githubusercontent.com/76394506/222956195-0dd600ca-100d-4cc1-b79d-4ea2d10b4304.png)

<p align='center'>
    <h1><strong>PRECIO🌿</strong></h1>
</p>

Precio is a comprehensive solution designed to assist modern farmers in optimizing their agricultural operations. This document serves as a guide for developers and users of Precio, providing information on the project's features, functionality, and usage.                                 The software is available under the MIT License.

## Purpose

Precio is an open-source software tool for monitoring, automating and visualizing farming data. It provides real-time data analysis and insights of farming, enabling informed decision-making and improving farming efficiency. Precio includes third-party integration and is designed to be user-friendly, optimizing resource usage, reducing waste, and increasing productivity.

## Audience

This application is intended for any agricultural enthusiast and developers looking forward for contributing into precision farming applications.

</br>
<hr/>

## Installation and Usage

- Clone the repository :\
  `git clone [https://github.com/suryan-s/Precio](https://github.com/suryan-s/Precio)`
- Run setup.py in the main directory to create virtual environment, install packages from requirements.txt and build the static files for the frontend:\
  `python setup.py`
- Run application by:\
  `uvicorn main:app --port 8000 --host 127.0.0.1`
</br>

<hr/>

## Files and Folders

```

Precio
├─ .gitignore
├─ .vscode
│  └─ settings.json
├─ arduino
│  ├─ PMS.ino
│  ├─ Weather Monitoring Station
│  │  ├─ WMS-GERBER-img.jpg
│  │  ├─ WMS-GERBER-PDF.pdf
│  │  ├─ WMS-GERBER-PNG.png
│  │  └─ WMS-GERBER.zip
│  └─ WMS.ino
├─ database
│  └─ .gitkeep
├─ endpoints.py
├─ frontend
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  └─ vite.svg
│  ├─ README.md
│  ├─ src
│  │  ├─ App.svelte
│  │  ├─ assets
│  │  │  └─ svelte.svg
│  │  ├─ lib
│  │  │  ├─ components
│  │  │  │  ├─ Button.svelte
│  │  │  │  ├─ Fab.svelte
│  │  │  │  ├─ Modal.svelte
│  │  │  │  └─ Sidebar.svelte
│  │  │  ├─ composites
│  │  │  │  ├─ CreateProject.svelte
│  │  │  │  ├─ Layout.svelte
│  │  │  │  └─ Sidenav.svelte
│  │  │  ├─ routes
│  │  │  │  ├─ dashboard.svelte
│  │  │  │  ├─ Home.svelte
│  │  │  │  └─ routes.js
│  │  │  └─ stores.js
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  └─ vite.config.js
├─ index.html
├─ LICENSE
├─ main.py
├─ model
│  └─ best_pretemp.h5
├─ requirements.txt
├─ settings.json
├─ setup.py
└─ _README.md

```

</br>

<hr/>

## Requirements

- Python 3.8.5 or higher
- Arduino IDE
- Node.js 16.15.4 or higher
- Libraries used:
  - Python: numpy, pandas, tensorflow, keras, uvicorn, fastapi, scikit-learn
  - Svelte, vite, svelte-spa-router
  - IBM Carbon Design System
  - NanoID
- Optional requirements:
  - Hardware support for PMS(Plant Monitoring System) and WMS(Weather Monitoring Station)
</br>

<hr/>

## Integration and Features

Precio offers the following features:

- Real-time monitoring of critical data required for the governance of farming operations.
- Intuitive visualization features for better data analysis and insights.
- Easy integration with third-party tools and devices.
- User-friendly interface for streamlined operations and reduced resource usage.
- Support for following farming practices for greater flexibility:
  - Arable farming
  - Hydroponic farming
  - Horticulture
  - Aquaponics
  - Vertical farming
- Support for actuators and actions for improved efficiency with Telegram integration:
  - Water pumps
  - Water heaters
  - Lights
  - Sprinklers
  - Irrigation systems
  - Ventilation systems
  - CO2 sensors
  - Temperature sensors
  - Humidity sensors
  - pH sensors
  - Water level sensors
  - Water flow sensors
  - Water quality sensors etc.
</br>

- IoT integration could be implemented by connecting to localhost/api/WMS/{api_token} or localhost/api/PMS/{api_token}

<hr/>

## Current Status

- [x] Create project and organise projects.
- [x] Support for Arable farming.
- [x] Visualization dashboard.
- [x] Integration with Arduino with hardware and software support for WMS.
- [x] Dockerized application.

## Future Developments

- [ ] Integration with Arduino with hardware and software support for PMS.
- [ ] Telegram integration for actuators and actions.
- [ ] ML model for predicting plant health and advanced predictions
- [ ] Support for Horticulture, Aquaponics, Vertical farming

## Contribution and Guidelines

To start contributing to the project, clone the repository into your local system subdirectory using the below git code:

```
https://github.com/suryan-s/Precio.git
```

Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key, or by using [Git CLI](https://cli.github.com/). The changes may additionally be performed by opening this repo using [GitHub Desktop](https://desktop.github.com/)

## Submitting a Pull Request

Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines.

Navigate to this subdirectory, & check status of all files that were altered (red) by running the below code in Git Bash:

```
  git status
```

Stage all your files that are to be pushed into your pull request. This can be done in two ways - stage all or some files:

```
  git add .            // adds every single file that shows up red when running git status
```

```
  git add <filename>   // type in the particular file that you would like to add to the PR
```

Commit all the changes that you've made and describe in brief the changes that you have made using this command:

```
  git commit -m "<commit_message>"
```

Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:

```
  git push origin main
```

</br>

<hr/>
