
# Docker Container wallstreetbets-sentiment-analysis

A docker container using restful endpoints exposed on port 5000 "/analyze" to gather sentiment analysis on the wsb subreddit.
* [Check out the main branch for non docker/web version](https://github.com/asad70/wallstreetbets-sentiment-analysis/tree/main)


## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Container Startup

List the different parameters available to your container

```shell
docker run -p 5000:5000 -e CLIENT_ID= -e CLIENT_SECRET= -e USERNAME= -e PASSWORD= restfulleo/wallstreetbets-sentiment-analysis
```

#### Environment Variables

* `CLIENT_ID` - A client_id from valid reddit account with a developer application setup.
* `CLIENT_SECRET` - A client_secret from that developer application setup for the reddit account.
* `USERNAME` - The username for the reddit account used above.
* `PASSWORD` - The password used for the reddit account.

#### Useful File Locations

* `/app` - source directory

## Built With

* astroid==2.4.2
* certifi==2020.12.5
* chardet==4.0.0
* click==7.1.2
* colorama==0.4.4
* cycler==0.10.0
* Flask==1.1.2
* idna==2.10
* isort==5.7.0
* itsdangerous==1.1.0
* Jinja2==2.11.2
* joblib==1.0.0
* kiwisolver==1.3.1
* lazy-object-proxy==1.4.3
* MarkupSafe==1.1.1
* matplotlib==3.3.3
* mccabe==0.6.1
* nltk==3.5
* numpy==1.19.5
* pandas==1.2.1
* Pillow==8.1.0
* praw==7.1.0
* prawcore==1.5.0
* pylint==2.6.0
* pyparsing==2.4.7
* python-dateutil==2.8.1
* pytz==2020.5
* regex==2020.11.13
* requests==2.25.1
* rope==0.18.0
* six==1.15.0
* squarify==0.4.3
* toml==0.10.2
* tqdm==4.56.0
* update-checker==0.18.0
* urllib3==1.26.2
* websocket-client==0.57.0
* Werkzeug==1.0.1
* wrapt==1.12.1

## Find Us

* [GitHub](https://github.com/asad70/wallstreetbets-sentiment-analysis)

## Authors

* **asad70** - *Initial work* - [PurpleBooth](https://github.com/asad70)
* **RestfulLeo23** - *Docker work* - [PurpleBooth](https://github.com/RestfulLeo23)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
