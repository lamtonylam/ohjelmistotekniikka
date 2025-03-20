from invoke import task


@task
def build(ctx):
    ctx.run("python3 src/db/initialize_database.py", pty=True)
