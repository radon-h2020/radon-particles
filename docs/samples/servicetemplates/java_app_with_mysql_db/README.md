## Java Application Connected to a MySQL Database


This sample service template models the following topology (no artifacts are provided):

```
my_java_application ---- ConnectsTo ---->  my_database
        |                                       |
     HostedOn                                HostedOn
        |                                       |
my_java_runtime                          my_mysql_server
        |                                       |
     HostedOn                                HostedOn
        |                                       |
my_application_server                   my_database_server
```

---