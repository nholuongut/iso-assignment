
# ISO Assignment

![](https://i.imgur.com/waxVImv.png)
### [View all Roadmaps](https://github.com/nholuongut/all-roadmaps) &nbsp;&middot;&nbsp; [Best Practices](https://github.com/nholuongut/all-roadmaps/blob/main/public/best-practices/) &nbsp;&middot;&nbsp; [Questions](https://www.linkedin.com/in/nholuong/)

![GitHub language count](https://img.shields.io/github/languages/count/ashleymichaelwilliams/aws-sandbox) ![GitHub top language](https://img.shields.io/github/languages/top/ashleymichaelwilliams/aws-sandbox)<br>
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![AquaSec](https://img.shields.io/badge/aqua-%231904DA.svg?style=for-the-badge&logo=aqua&logoColor=#0018A8) !
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
<br>

## Task
The task was to create microservice, that is able to take an country ISO code and a list of country names (in different languages) as an input. It will filter out just the countries that correspond to the provided ISO code.

Serve the application as the API.

## Disclaimer
The countries has to be in right format for given language, on the other hand, iso is not a case sensitive parameter. Supports both, 3166-1 alpha-2 and ISO 3166-1 alpha-3. Also, it does not preserve the order of "out filtered" countries, can be changed in code by uncommenting one single line.

This code was developed on Windows 10 running Python 3.10.2
## API Reference

#### Make request example

```
  POST http://127.0.0.1:8000/match_country
```

```
{
        "iso": "fra",
        "countries": [
                "Slovakia",
                "Slovensko", 
                "Czechia", 
                "Česko", 
                "Botswana", 
                "Taiwan", 
                "Francúzsko", 
                "Frankreich",
                "France", 
                "Francie"
        ]
}
```

#### Will return :

```
{
        "iso": "fra",
        "match_count": 4,
        "matches": [
                "Frankreich",
                "Francúzsko",
                "France",
                "Francie"
        ]
}
```

Swagger can be accessed at: http://127.0.0.1:8000/redoc

## Run Locally

Clone the project

```bash
  git clone https://github.com/nholuongut/iso-assignment.git
```

Go to the project directory

```bash
  cd iso-assignment
```

Use docker

```bash
  docker-compose up
```


## Running Tests

To run tests, run the following command

```bash
  docker exec -it fastapi pytest
```

If you would like to add tests of your own, modify **test_api.py** file


## FE

This project also contains FE app, *pyscript.html,* so you can engage with the API interactively in your browser.

![example.png](https://i.postimg.cc/zvGwxLQZ/example.png)

I'm are always open to your feedback.  Please contact as bellow information:
### [Contact ]
* [Name: nho Luong]
* [Skype](luongutnho_skype)
* [Github](https://github.com/nholuongut/)
* [Linkedin](https://www.linkedin.com/in/nholuong/)
* [Email Address](luongutnho@hotmail.com)

![](https://i.imgur.com/waxVImv.png)
![](bitfield.png)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nholuong)

# License
* Nho Luong (c). All Rights Reserved.


