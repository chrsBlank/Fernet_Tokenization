# Fernet Tokenization
## _Server_ _managed_ , _in_ _YOUR_ _database_


I really dont like JWT, since I believe it has some major security problems, so since i needed a tokenization method, i made my own

- Using Fernet encryption
- Stored locally
- Nearly impossible to hand craft
- In python
- Leveraging MariaDB for speedy insertions/search

## Libraries Used

- [Fernet] - cryptography.fernet
- [Datetime] - datetime
- [MariaDB Connector] - mariadb
- [Relative Delta] - dateutil.relativedelta 
- [PathLib] - pathlib

## Usage

To generate your fernet key you can use this

```py
from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

print(key)
```
The generation was found [here] 

Save the key in a file called filekey.key in the same directory as the Fetok.py file and your script

##

Import the Fertok.py as a library

```py
import Fertok
```
and use the functions of the module in your python script just like any other library

## License

Apache Lincense 2.0

[here]: <https://cryptography.io/en/latest/fernet/>
[Fernet]: <https://cryptography.io/en/latest/fernet/>
[Datetime]: <https://docs.python.org/3/library/datetime.html>
[MariaDB Connector]: <https://mariadb.com/kb/en/about-mariadb-connector-python/>
[Relative Delta]: <https://dateutil.readthedocs.io/en/stable/relativedelta.html>
[PathLib]: <https://docs.python.org/3/library/pathlib.html>

