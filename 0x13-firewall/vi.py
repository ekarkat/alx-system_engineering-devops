from fabric import Connection


con = Connection("alx1")

con.run("sudo cat befoore.rules")