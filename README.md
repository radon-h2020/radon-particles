# RADON Particles

> TOSCA definitions repository for the [RADON project](http://radon-h2020.eu)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![RADON on Twitter](https://img.shields.io/twitter/url/https/twitter.com/RADON_2020?label=RADON%20on%20Twitter&style=social)](https://twitter.com/RADON_2020)

The RADON Particles repository contains TOSCA blueprints, reusable definitions and extensions to deploy and manage RADON applications.
It provides reusable TOSCA types of application runtimes, computing resources, and FaaS platforms in the form of abstract as well as deployable modeling entities.
The repository also comprises RADON's FaaS abstraction layer that provides several TOSCA definitions to deploy a particular FaaS application component to different cloud providers.

---

Node types in this public repository are in a certain state of development, indicated by the following badges:
* ![](https://img.shields.io/badge/Status:-DEVELOPMENT-red) - initially published or currently under development
* ![](https://img.shields.io/badge/Status:-TESTING-yellow) - current version working under certain conditions
* ![](https://img.shields.io/badge/Status:-RELEASED-green) - working as described
* ![](https://img.shields.io/badge/Status:-DEPRECATED-inactive) - no longer supported

Further, node types having a ![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet) badge indicate that they represent a resource that can be actually deployed using a TOSCA orchestrator supporting Ansible implementations, such as [xOpera](https://github.com/xlab-si/xopera-opera).
