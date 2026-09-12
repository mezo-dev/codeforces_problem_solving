from typing import Union


class DBServer1:
    def __repr__(self):
        return "DB Server 1"


class DBServer2:
    def __repr__(self):
        return "DB Server 2"


class DBServer3:
    def __repr__(self):
        return "DB Server 3"


# A hash function is basically a function that takes some input and turns it into another value used to locate something.

def get_user_from_server(user_id: int) -> Union[DBServer1, DBServer2, DBServer3]:
    servers = {
        1: DBServer1(),
        2: DBServer2(),
        3: DBServer3()
    }

    server_number = user_id % len(servers) + 1

    return servers[server_number]


print(get_user_from_server(
    4
))