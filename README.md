Django Config Generator
=========================
A simple Python script for creating default configs for Django + Gunicorn + 
Nginx stack that I use in my projects. Project variables are stored in 
`project_info.py` and then inserted into the configs.

They follow my project structure, and they pretty much the opposite of 
'universal' because of that. But feel free to point out a better structure or 
propose a way to make it more configurable.

## Project tree
```
.
├── app                     <- Repo
│   ├── media
│   ├── README.md
│   ├── requirements.txt
│   ├── src                 <- Django app
│   │   ├── manage.py
│   │   └── ...
│   └── static
├── bin                     <- Virtualenv
├── include                 <- Virtualenv
├── lib                     <- Virtualenv
├── log                     <- All logs
└── run                     <- Gunicorn socket
```

## Usage
To use the script, clone the repository:  
```
$ git clone https://github.com/pawelad/django-config-generator.git
$ cd django-config-generator
```

Then put your project info into `project_info.py` and run the script:  
`$ python3 django_config_generator.py`

Your config files are now generated. You can move them to proper directories by
running printed commands.
