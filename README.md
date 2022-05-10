<!-- PROJECT SHIELDS -->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

-->
[![GitHub license](https://img.shields.io/github/license/Winkii/MineBot-online-players)](https://github.com/Winkii/MineBot-online-players)
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Winkii/MineBot-online-players">
    <img src="https://github.com/Winkii/MineBot-online-players/blob/main/Ressources/img/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MineBot Online Players</h3>

  <p align="center">
    This is a Discord Webhook that sends a message when a user connects or disconnects on the Minecraft Server
    <br />
  </p>
</p>

If you want to support me, thank you !<br>
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G2BJ2E7)
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#requirements">Requirements</a>
    </li>
    <li>
      <a href="#configuration-file">Configuration file</a>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a Discord Webhook that sends a message when a user connects or disconnects on the Minecraft Server.

<!-- GETTING STARTED -->
## Requirements
Only Java servers are supported.
Language : Python3<br>
### Librairies required
   ```sh
pip install -r requirements.txt
   ```
### Configure Discord Webhook
In Discord, select the Server, under Text Channels, select Edit Channel (gear icon)

Select Integrations > View Webhooks and click New Webhook.

Copy the Webhook URL and paste in the ```params.conf``` file.
```txt
url=link_of_webhook
```


## Configuration file
The configuration file is ```params.conf```

 | Variable Name                               |   Description
 | ------------------------------------------- |:-----------------------------
 | server                                      | FQDN or IP of the Minecraft Server
 | server_port                                 | Listening port of the Minecraft Server
 | url                                         | Discord Webhook URL (<a href="#configure-discord-webhook">Here</a>)
 | delay                                       | Delay of the check 

<!-- USAGE EXAMPLES -->
## Usage
Before launch the MineBot, you need to modify ```params.conf```
Use this command for execute the MineBot Online Players.
```sh
git clone https://github.com/Winkii/MineBot-online-players
cd MineBot-online-players
python3 main.py
```

## Incoming Features
⏳ Launch as a service


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555 -->
<!--[linkedin-url]: https://linkedin.com/in/github_username-->
