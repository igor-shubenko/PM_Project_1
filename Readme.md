## Project description

**Starting services**

Clone repo to local directory and run 

```commandline
docker compose up
```

This command starts services in docker compose: 

1. ***postgres***  - database with tables (Users, Bets, Events), filled some data on startup
2. ***kafka*** - message broker
3. ***init-topics*** - creates topics **events.taxonomy** and **bets.state**, then exits 
4. ***events_api_server*** - server for providing event CRUD operations
5. ***crud_server*** - server for providing user and bet CRUD operations
6. ***event_writer_consumer*** - reads **event_info** from **events.taxonomy** and adds them into database
7. ***bet_scorer_consumer***  - reads **event_info** from **events.taxonomy**, reads bets of event from database,
change bets state, pushes changed **bets_info** to **bets.state** topic
8. ***bet_writer_consumer*** - reads **bet_info** from **bets.state** and updates bets records in database


**Events_api_server**

Starts on _localhost:8767_

Endpoints for working with table _Events_

- ***/event/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/event/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/event/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/event/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.

**Crud_server**

Starts on _localhost:8765_

Endpoints for working with table _Users_

- ***/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.

Endpoints for working with table _Bets_

- ***/bet/get/{idn}*** - HTTP method must be GET. _{idn}_ - record _id_ (integer) in table, or 'all' for getting all records from table.
- ***/bet/add*** - HTTP method must be POST. Expect json data in request's body. Fields 'name' and 'time_created' are required.
- ***/bet/change/{idn}*** - HTTP method must be PUT. _{idn}_ - record _id_ (integer) in table. Expect json data in request's body.
- ***/bet/delete/{idn}*** - HTTP method must be DELETE. _{idn}_ - record _id_ (integer) in table , or 'all' for deleting all records from table.
