# django-dead
Django Easy Applications Development

**Usage:**

* Install package:
    ```bash
    pip install -U git+https://github.com/000paradox000/django-dead.git
    ```
  
* Update django-dead package:
    ```bash
    dead-admin.py -u
    ```

* Delete django project:
    ```bash
    dead-admin.py -d
    ```

* Install operating system dependencies:
    ```bash
    dead-admin.py -o
    ```

* Install pip dependencies:
    ```bash
    dead-admin.py -p
    ```

* Create new django project:
    ```bash
    dead-admin.py -c
    ```

* Make migrations and migrate django project:
    ```bash
    dead-admin.py -m
    ```

* Run project in 0.0.0.0:9500:
    ```bash
    dead-admin.py -l
    ```

* Create system users:
    ```bash
    dead-admin.py -s
    ```
    * pk: 1, username: system, is_active: False
    * pk: 2, username: admin, password: admin, is_superuser: True

* Create a new template based django project (DEAD project):

    ```bash
    dead-admin.py -t "basic" "myproject" "DEAD" "My DEAD Project" "dead.000paradox000.pes" "dead@000paradox000.pes" "12345" "info@000paradox000.pes"
    ```
    
    **Arguments:**

    * **template_name:** basic
    * **slug:** slug name for the project. This is used for naming many items like the static_url, media_url, etc
    * **short_title:** this title is used by the basic template in the navbar brand place
    * **long_title:** this title is used by the basic template in the footer
    * **domain:** http domain used by the project when running in production
    * **email:** email account used byt the project for sending messages
    * **password:** email account password
    * **email_bcc_recipient:** main bcc recipient of the messages sent by the project
