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

## License

Apache Lincense 2.0

